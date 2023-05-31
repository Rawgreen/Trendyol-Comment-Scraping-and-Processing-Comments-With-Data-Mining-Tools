import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from TurkishStemmer import TurkishStemmer
from nltk.corpus import stopwords
import string
import re

# Read the XLSX file
df = pd.read_excel("5K Raw Data0000.xlsx")

# Create a Turkish stemmer
stemmer = TurkishStemmer()

# Load Turkish stopwords
nltk.download('stopwords')
stopwords = set(stopwords.words('turkish'))

"""
Same logic for all functions but specified to given scenario number.
Written like this in order to avoid mistakes.
"""
def preprocess1111(text):
    # Lowercase the text
    text = text.lower()

    # Remove emoticons
    text = re.sub(r'<:[a-zA-Z0-9_]+:>', '', text)

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize the text into words using word_tokenize()
    tokens = word_tokenize(text, language='turkish')

    # Perform stemming using the TurkishStemmer
    filtered_tokens = [stemmer.stem(token) for token in tokens]

    # Remove stopwords
    filtered_tokens = [token for token in filtered_tokens if token not in stopwords]

    # Join the processed tokens back into a single string
    preprocessed_text = ' '.join(filtered_tokens)

    return preprocessed_text
def preprocess1110(text):
    # Lowercase the text
    text = text.lower()

    # Remove emoticons
    text = re.sub(r'<:[a-zA-Z0-9_]+:>', '', text)

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize the text into words using word_tokenize()
    tokens = word_tokenize(text, language='turkish')

    # Perform stemming using the TurkishStemmer
    filtered_tokens = [stemmer.stem(token) for token in tokens]

    # Join the processed tokens back into a single string
    preprocessed_text = ' '.join(filtered_tokens)

    return preprocessed_text
def preprocess1101(text):
    # Lowercase the text
    text = text.lower()

    # Remove emoticons
    text = re.sub(r'<:[a-zA-Z0-9_]+:>', '', text)

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize the text into words using word_tokenize()
    tokens = word_tokenize(text, language='turkish')

    # Remove stopwords
    filtered_tokens = [token for token in tokens if token not in stopwords]

    # Join the processed tokens back into a single string
    preprocessed_text = ' '.join(filtered_tokens)

    return preprocessed_text
def preprocess1100(text):
    # Lowercase the text
    text = text.lower()

    # Remove emoticons
    text = re.sub(r'<:[a-zA-Z0-9_]+:>', '', text)

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize the text into words using word_tokenize()
    tokens = word_tokenize(text, language='turkish')

    # Join the tokens back into a single string
    preprocessed_text = ' '.join(tokens)

    return preprocessed_text
def preprocess1011(text):
    # Lowercase the text
    text = text.lower()

    # Remove emoticons
    text = re.sub(r'<:[a-zA-Z0-9_]+:>', '', text)

    # Tokenize the text into words using word_tokenize()
    tokens = word_tokenize(text, language='turkish')

    # Perform stemming using the TurkishStemmer
    filtered_tokens = [stemmer.stem(token) for token in tokens]

    # Remove stopwords
    filtered_tokens = [token for token in filtered_tokens if token not in stopwords]

    # Join the processed tokens back into a single string
    preprocessed_text = ' '.join(filtered_tokens)

    return preprocessed_text
def preprocess1010(text):
    # Lowercase the text
    text = text.lower()

    # Remove emoticons
    text = re.sub(r'<:[a-zA-Z0-9_]+:>', '', text)

    # Tokenize the text into words using word_tokenize()
    tokens = word_tokenize(text, language='turkish')

    # Perform stemming using the TurkishStemmer
    filtered_tokens = [stemmer.stem(token) for token in tokens]

    # Join the processed tokens back into a single string
    preprocessed_text = ' '.join(filtered_tokens)

    return preprocessed_text
def preprocess1001(text):
    # Lowercase the text
    text = text.lower()

    # Remove emoticons
    text = re.sub(r'<:[a-zA-Z0-9_]+:>', '', text)

    # Tokenize the text into words using word_tokenize()
    tokens = word_tokenize(text, language='turkish')

    # Remove stopwords
    filtered_tokens = [token for token in tokens if token not in stopwords]

    # Join the processed tokens back into a single string
    preprocessed_text = ' '.join(filtered_tokens)

    return preprocessed_text
def preprocess1000(text):
    # Lowercase the text
    text = text.lower()

    # Remove emoticons
    text = re.sub(r'<:[a-zA-Z0-9_]+:>', '', text)

    # Tokenize the text into words using word_tokenize()
    tokens = word_tokenize(text, language='turkish')

    # Join the processed tokens back into a single string
    preprocessed_text = ' '.join(tokens)

    return preprocessed_text
def preprocess0111(text):
    # Remove emoticons
    text = re.sub(r'<:[a-zA-Z0-9_]+:>', '', text)

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize the text into words using word_tokenize()
    tokens = word_tokenize(text, language='turkish')

    # Perform stemming using the TurkishStemmer
    filtered_tokens = [stemmer.stem(token) for token in tokens]

    # Remove stopwords
    filtered_tokens = [token for token in filtered_tokens if token not in stopwords]

    # Join the processed tokens back into a single string
    preprocessed_text = ' '.join(filtered_tokens)

    return preprocessed_text
def preprocess0110(text):
    # Remove emoticons
    text = re.sub(r'<:[a-zA-Z0-9_]+:>', '', text)

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize the text into words using word_tokenize()
    tokens = word_tokenize(text, language='turkish')

    # Perform stemming using the TurkishStemmer
    filtered_tokens = [stemmer.stem(token) for token in tokens]

    # Join the processed tokens back into a single string
    preprocessed_text = ' '.join(filtered_tokens)

    return preprocessed_text
def preprocess0101(text):
    # Remove emoticons
    text = re.sub(r'<:[a-zA-Z0-9_]+:>', '', text)

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize the text into words using word_tokenize()
    tokens = word_tokenize(text, language='turkish')

    # Join the tokens back into a single string
    preprocessed_text = ' '.join(tokens)

    return preprocessed_text
def preprocess0100(text):
    # Remove emoticons
    text = re.sub(r'<:[a-zA-Z0-9_]+:>', '', text)

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize the text into words using word_tokenize()
    tokens = word_tokenize(text, language='turkish')

    # Join the tokens back into a single string
    preprocessed_text = ' '.join(tokens)

    return preprocessed_text
def preprocess0011(text):
    # Remove emoticons
    text = re.sub(r'<:[a-zA-Z0-9_]+:>', '', text)

    # Tokenize the text into words using word_tokenize()
    tokens = word_tokenize(text, language='turkish')

    # Perform stemming using the TurkishStemmer
    filtered_tokens = [stemmer.stem(token) for token in tokens]

    # Remove stopwords
    filtered_tokens = [token for token in filtered_tokens if token not in stopwords]

    # Join the processed tokens back into a single string
    preprocessed_text = ' '.join(filtered_tokens)

    return preprocessed_text
def preprocess0010(text):
    # Remove emoticons
    text = re.sub(r'<:[a-zA-Z0-9_]+:>', '', text)

    # Tokenize the text into words using word_tokenize()
    tokens = word_tokenize(text, language='turkish')

    # Perform stemming using the TurkishStemmer
    filtered_tokens = [stemmer.stem(token) for token in tokens]

    # Join the processed tokens back into a single string
    preprocessed_text = ' '.join(filtered_tokens)

    return preprocessed_text
def preprocess0001(text):
    # Remove emoticons
    text = re.sub(r'<:[a-zA-Z0-9_]+:>', '', text)

    # Tokenize the text into words using word_tokenize()
    tokens = word_tokenize(text, language='turkish')

    # Join the tokens back into a single string
    preprocessed_text = ' '.join(tokens)

    return preprocessed_text

# Apply preprocessing to the desired column(s) in the DataFrame
df['Preprocessed Text'] = df['Comment'].apply(preprocess0001)
# Replace 'Comment' with the actual column name containing the text you want to preprocess

# Save the updated DataFrame back to the XLSX file
df.to_excel("5K Data0001.xlsx", index=False)
# Replace '5K Raw Data.xlsx' with the desired filename for the outputting preprocessed data