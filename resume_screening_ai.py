import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout , Bidirectional,GRU
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.utils import to_categorical

data = pd.read_csv('UpdatedResumeDataSet.csv')
data.sample(3)

data.shape

data["Resume"][100]

# converting to lower case
data["Resume"] = data["Resume"].str.lower()
data["Category"] = data["Category"].str.lower()

data.sample(2)

import re

# removing the html tages

def remove_html_tage(text):
  if isinstance(text,str):
    pattern = re.compile("<.*?>")
    return pattern.sub("",text)

data["Resume"] = data["Resume"].apply(remove_html_tage)

def remove_link(text):
  if isinstance(text,str):
    pattern = re.compile(r'https?://\S+|www\.\S+')
    return pattern.sub("",text)

remove_link("i am amit https://colab.research.google.com/drive/19eZJz2Jdal4OqxFjWdQdQBuVZ6hvcBkF#scrollTo=nmKmlJxhPswv ")

data["Resume"] = data["Resume"].apply(remove_link)

def replace_special_char(q):

    q = q.replace('$', ' dollar ')
    q = q.replace('₹', ' rupee ')
    q = q.replace('€', ' euro ')
    q = q.replace('@', ' at ')

    # Replacing some numbers with string equivalents (not perfect, can be done better to account for more cases)
    q = q.replace(',000,000,000 ', 'b ')
    q = q.replace(',000,000 ', 'm ')
    q = q.replace(',000 ', 'k ')
    q = re.sub(r'([0-9]+)000000000', r'\1b', q)
    q = re.sub(r'([0-9]+)000000', r'\1m', q)
    q = re.sub(r'([0-9]+)000', r'\1k', q)
    return q

data["Resume"] = data["Resume"].apply(replace_special_char)

import string
pn = string.punctuation
pn

# remove the punctutation
def remove_punc(text):
  if isinstance(text,str):
    return text.translate(str.maketrans("","",pn))

data["Resume"] = data["Resume"].apply(remove_punc)

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

stop_words = stopwords.words('english')

def removing_stop_word(text):
  if isinstance(text,str):
    return " ".join([word for word in text.split() if word not in stop_words])

# removing_stop_word("hi i am amit")

data["Resume"] = data["Resume"].apply(removing_stop_word)

data["Resume"][98]

def remove_spical_symboles(text):
  if isinstance(text,str):
    pattern = re.compile(r'[^a-zA-Z0-9\s]')
    return pattern.sub("",text)

data["Resume"] = data["Resume"].apply(remove_spical_symboles)

# remove extra spaces
def rmove_extra_space(text):
  text = re.sub(r'[^\x00-\x7f]',' ',text)
  text = re.sub(r'\s+', ' ', text)
  return text

data["Resume"] = data["Resume"].apply(remove_spical_symboles)

data["Resume"]

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
data["label"] = le.fit_transform(data['Category'])

x = data["Resume"]
y = data["label"]

from nltk.tokenize import word_tokenize,sent_tokenize

nltk.download('punkt')

from tensorflow.keras.preprocessing.text import Tokenizer

tokenizer = Tokenizer(num_words=10000,oov_token="<OOV>")
tokenizer.fit_on_texts(x)

seq = tokenizer.texts_to_sequences(x)

max_len = 300
max_len

pad_seq = pad_sequences(seq,maxlen=max_len,padding="post",truncating="post")

pad_seq.shape

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(pad_seq,y,test_size = 0.2,random_state = 42)

print(data["Category"].value_counts())

voc_size = len(tokenizer.word_index)+1

from tensorflow.keras.layers import Input

# Building Modle

model = Sequential()

model.add(Input(shape=(max_len,)))

model.add(Embedding(input_dim=voc_size, output_dim=128))

model.add(Bidirectional(GRU(128)))

#model.add(Dropout(0.2))

model.add(Dense(64, activation='relu'))

model.add(Dense(len(data["label"].unique()), activation='softmax'))

model.summary()

model.compile(loss="sparse_categorical_crossentropy",
                        optimizer = "adam",
                        metrics = ["accuracy"])

early_stop = EarlyStopping(
    monitor = "val_loss",
    patience = 3,
    restore_best_weights=True,
    verbose = 1
)

history = model.fit(
    x_train,
    y_train,
    epochs=20,
    batch_size=32,
    validation_split=0.2,
    callbacks = [early_stop]
)

loss, accuracy = model.evaluate(x_test, y_test)

print("Accuracy:", accuracy)

model.save("resume_screening_model1.h5")

model.save("resume_model2.keras")

plt.plot(history.history["accuracy"])
plt.plot(history.history["val_accuracy"])

plt.plot(history.history["loss"])
plt.plot(history.history["val_loss"])

pred = model.predict(x_test)



y_pred = pred.argmax(axis=1)

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

cm

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12,8))

sns.heatmap(cm, annot=True, fmt='d')

plt.xlabel("Predicted")

plt.ylabel("Actual")

plt.show()

sample_resume = """
John Smith

Professional Summary:
Experienced Machine Learning Engineer and AI Developer with 3+ years of experience
building deep learning, NLP, and computer vision applications. Skilled in Python,
TensorFlow, PyTorch, Scikit-learn, and Flask API development.

Technical Skills:
- Python
- TensorFlow
- Keras
- PyTorch
- Machine Learning
- Deep Learning
- NLP
- Computer Vision
- Pandas
- NumPy
- Scikit-learn
- Flask
- FastAPI
- SQL
- Git
- Docker

Experience:
Worked on multiple AI-based applications including resume screening systems,
chatbots, recommendation systems, and image classification projects.
Developed NLP pipelines for text preprocessing, tokenization, embedding,
and sentiment analysis.

Built deep learning models using CNN, LSTM, and Transformer architectures.
Integrated machine learning models with Flask and FastAPI for deployment.

Projects:
1. Resume Screening AI
- Developed an NLP-based resume classification system using TensorFlow and LSTM.
- Achieved high classification accuracy on multiple job categories.

2. AI Chatbot
- Built an intelligent chatbot using NLP and deep learning techniques.

3. Image Classification System
- Trained CNN models for image recognition and classification tasks.

Education:
Bachelor of Computer Science

Certifications:
Deep Learning Specialization
Machine Learning Certification
"""


sample_resume = sample_resume.lower()

sample_resume = remove_html_tage(sample_resume)

sample_resume = remove_link(sample_resume)

sample_resume = replace_special_char(sample_resume)

sample_resume = remove_punc(sample_resume)

#sample_resume = removing_stop_word(sample_resume)

sample_resume = remove_spical_symboles(sample_resume)

sample_resume = rmove_extra_space(sample_resume)

sample_seq = tokenizer.texts_to_sequences([sample_resume])

sample_pad = pad_sequences(
    sample_seq,
    maxlen=300,
    padding='post',
    truncating='post'
)

pred = model.predict(sample_pad)

predicted_label = pred.argmax(axis=1)

predicted_label

predicted_role = le.inverse_transform(predicted_label)

print(predicted_role)

confidence = pred.max() * 100

print("Confidence:", confidence)

pred = model.predict(sample_pad)

top_5 = pred[0].argsort()[-5:][::-1]

for i in top_5:

    role = le.inverse_transform([i])[0]

    confidence = pred[0][i] * 100

    print(f"{role} --> {confidence:.2f}%")
