import pandas as pd
import spacy
import re
from tqdm import tqdm
from utils import word_tag_pairs
from utils import extract_email_msg
from utils import imperative_sentences
nlp = spacy.load('en_core_web_sm')



data = pd.read_csv(r'emails.csv',encoding = 'utf-8-sig')

contents = extract_email_msg(data)
data["email_contents"] = contents
print(len(contents))

results = []
for text in tqdm(data["email_contents"].tolist()):
    temp = re.sub('\n', '', text)
    doc = nlp(temp)
    results.append(imperative_sentences(word_tag_pairs(doc)))

data["contains_actionable"] = results
# data.to_csv(r'path/to/directory')
