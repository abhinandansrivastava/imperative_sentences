# Objective 1
Detect whether sentence contains actionable chunks with Rule Based Chunking
---------------------------------------------------------------------------

In this Project, we are trying to find whether the email contains any actionable items or not.
Basically those kind sentences are imperative in nature.
---------------------------------------------------------------------------
## Logic
Case:1
if its an interrogative sentence:
	if pos_tags starts with ["VB","MD","VBP"]:
		actionable_sentences = True
	else:
		the chunk is Verb Phrase:
			actionable_sentences = True
else:
	if the sentence starts with "please/kindly" like words:
		actionable_sentences = True

---------------------------------------------------------------------------
Test Via Flask API
```python app.py```
---------------------------------------------------------------------------

# Objective 2
Use the output from objective 1 and Train a ML Model for predicting actionable sentences.

## Logic 1:
### BERT Binary Classification 
```
recall:0.9796
precision:1.0000
F1 measure:0.9897
```

## Logic 2:
### TFIDF + Logistic Regression
```
recall:0.8070
precision:0.9583
F1 measure:0.8762
```

## Future work:
add more cases for imperative sentences
Multi threading

---------------------------------------------------------------------------

## Reference:
https://spacy.io/usage/linguistic-features#dependency-parse
https://examples.yourdictionary.com/imperative-sentence-examples.html
https://www.englishclub.com/grammar/sentence/type-imperative.htm
StackOverflow