import pandas as pd
import json
import csv
import pickle
import random
import h5py
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

#__________________________________This file trains the machine learning model with the user inputs_______________________________


lemmatizer = WordNetLemmatizer()

#Import JSON file of inputs

intents = json.loads(open("intents.json").read())

#create empty lists
words = []
classes = []
documents = []

#iterating through intents and tokenize the words
for intent in intents['intents']:
    
    for pattern in intent['patterns']:
        word_list =nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
#print(documents)

words = [lemmatizer.lemmatize(word) for word in words]

#Put it in a list & turn it back into a list and sort it then eliminate duplicates
words = sorted(set(words))

#Save sorted words list as a pckl file 
classes= sorted(set(classes))
pickle.dump(words,open('words.pkl','wb'))
pickle.dump(classes,open('classes.pkl','wb'))


#Need to represent the words as numerical values using bag of words

training = []
output_empty = [0]* len(classes)

#running this loop will put all of the document data in the training list
for doc in documents:
    bag = []
    word_patterns = doc[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row])

#create a training list (split it into x & y values)
random.shuffle(training)
training = np.array(training)

train_x = list(training[:, 0])
train_y = list(training[:, 1])

#start to build the neural network model
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
#prevent overfitting 
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))

#we need as many neurons as their are training data inputs, hence len
#softmax activation function allows us to add up the results 
model.add(Dense(len(train_y[0]), activation='softmax'))

#Set up paramaters for learning rate, decay, momentum
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
#compile the model 
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose = 1)
#Save everything
model.save("chatbot_model.h5",hist)
print("done")

