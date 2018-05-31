import numpy

from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence

#ix random seed for reproducibility
numpy.random.seed(7)

#load the dataset but only keep the top n words, zero the rest
top_words = 50
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=top_words)
print("...Data Loaded")

#truncate and pad input sequences
max_review_length = 5
x_train = sequence.pad_sequences(x_train, maxlen=max_review_length)
x_test = sequence.pad_sequences(x_test, maxlen=max_review_length)

#create the model
embedding_vector_lenth = 32
model =  Sequential()
model.add(Embedding(top_words, embedding_vector_lenth, input_length=max_review_length))
model.add(LSTM(100))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())
model.fit(x_train, y_train, epochs=3, batch_size=64)

#Final evaluation of the model
scores =  model.evaluate(x_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[0]*100))
print("Accuracy: %.2f%%" % (scores[1]*100))
