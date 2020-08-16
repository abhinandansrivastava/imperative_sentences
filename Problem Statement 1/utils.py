import re
import spacy
import email
from tqdm import tqdm
import nltk
from nltk import RegexpParser
from nltk.tree import Tree
from nltk.tokenize import word_tokenize, sent_tokenize

def verb_phrase(pos_tag_sents):
    """
    Rules for Verb Phrases:
        DET+VERB-BASE
        ADVERB+VERB-BASE
        INJT+VERB-BASE
        INJT+VERB-BASE
    """
    verb_chunk = r"""VB-Phrase: {<DT><,>*<VB>}
                    VB-Phrase: {<RB><VB>}
                    VB-Phrase: {<UH><,>*<VB>}
                    VB-Phrase: {<UH><,><VBP>}
                    VB-Phrase: {<PRP><VB|VBP>}
                    VB-Phrase: {<NN.?>+<,>*<VB|MD>}"""
    chunkparser = RegexpParser(verb_chunk)
    return chunkparser.parse(pos_tag_sents)


def extract_email_msg(df):
    """
    :param df: dataframe containing the mails
    :return: contents of the messages
    """
    messages = []
    for item in tqdm(df["message"]):
        msg = email.message_from_string(item)
        contents = msg.get_payload()
        contents = contents.lower()
        messages.append(contents)
    return messages


def word_tag_pairs(doc):
    """
    :param doc: nlp pipe from spacy
    :return: tuple pairs with text,tag
    """
    word_tuple = []
    for token in doc:
        word_tuple.append((token.text,token.tag_))
    return word_tuple


def imperative_sentences(tagged_sent):
    """
    :param tagged_sent: tuple pairs with text,tag
    :return: contents of the messages
    """
    # for non-interrogative sentences
    if tagged_sent[-1][0] != "?": 
        if tagged_sent[0][1] == "VB" or tagged_sent[0][1] == "MD" or tagged_sent[0][1] == "VBP": #checking whether the first token contains VERB Phrases
            return True

        else:
            chunk = verb_phrase(tagged_sent)
            if type(chunk[0]) is Tree and chunk[0].label() == "VB-Phrase": #if first chunk is verb phrase
                return True

    # Interrogative type sentences
    else:
        pls = len([w for w in tagged_sent if w[0].lower() == "please"]) > 0 #if the sentences starts with please

        if pls or (tagged_sent[0][1] == "VB" or tagged_sent[0][1] == "MD"):
            return True

    return False