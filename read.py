import re

from SimpleTokenizer import SimpleTokenizerV1

#Convert text into token

with open("the-verdict.txt","r",encoding="utf-8") as f:
     raw_text = f.read()
print("Total number of character:", len(raw_text))
# print(raw_text[:99])

#preparing the token
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()] 
print(len(preprocessed))
print(preprocessed[:30])

#build vocabulary
all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
print(vocab_size)

#print 50 words from the vocabulary 
vocab = {token: integer for integer, token in enumerate(all_words)}
for i, item in enumerate(vocab.items()):
     print(item)
     if i>= 50:
          break


print ("### SimpleTokenizer")
tokenizer = SimpleTokenizerV1(vocab)
text = """"It's the last he painted, you know,"
        Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)
print(ids)

print(tokenizer.decode(ids))

print ("### new text sample not contained in the training set")
text = ""