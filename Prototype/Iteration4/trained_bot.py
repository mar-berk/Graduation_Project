#Import the libraries
import json
import pickle
import random
import h5py
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
import tensorflow as tf
from tensorflow.keras.models import load_model
from neuralintents import GenericAssistant

from textblob import TextBlob
import sys
import pandas as pd
import string

#__________________________ Setting up the training data _________________________

lemmatizer = WordNetLemmatizer()

#Import the IntentsJSON
intents = json.loads(open("intents.json").read())
#Import the nlp words, classes & training model
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))
model = load_model('chatbot_model.h5')

#clean user input 
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words
#convert sentence into bag of words
def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, in enumerate(words):
            if word ==w:
                bag[i]=1
    return np.array(bag)

        
#predicting results based on bag of words
def predict_class(sentence):
    bow =bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    #Only return results with a confidence level above .25
    ERROR_THRESHOLD =0.25
    result = [[i,r] for i,r in enumerate (res) if r> ERROR_THRESHOLD]
    #sort by probability
    results.sort(key=lambda x: x[1], reverse=True)
    #create a return list full of classes & probabilites
    return_list=[]
    for r in results:
        return_list.append({'intent':classes[r[0]], 'probability':str(r[1])})
    return return_list



#_______________________________________________CHATBOT SETUP__________________________________________________

# _________________________randomize energy tips_________________________

#Energy tips list
tips = [
    '\nDid you know that the Netherlands uses dynamic pricing for energy tariffs? For more info click here:https://www.energieprijzen-vergelijken.nl/energie/dynamische-tarieven/ \nThis means that by postponing heavy energy use such as showering, running the dishwasher, or washing clothes until the hours between 23:00 and 7:00 on weekdays or all day on the weekend, you can save money. \nYou will need to contact your energy provider to find out details about the rates available to you. ',
    "\nDuring warmer months, close blinds, shades and drapes on the sunny side of your home to help keep your home's temperature cooler and reduce the work for your AC. Open shades during cooler months to let the sun warm your home",
    "\nDid you know that many appliances are using energy even when they are 'turned off'? I highly recommend that you take a walk around your house and unplug everything that's not in use... make sure to inform your housemates & family members of this as well! For more detailed information click here: https://20somethingfinance.com/electrical-leaking-standby-appliance-list/ ",
    '\nTo view some general energy saving tips click  here: https://www.energieaanbieding.nl/bespaartips/',
    '\nPlace your refrigerator away from direct sunlight or heat sources in a well-ventilated area, to increase its energy efficiency. ',
    "\nAvoid opening the oven while it's cooking. Each time you do this the oven can lose up to 4 degrees of heat!",

]
#Randomize tips
def randomTips():
  info= random.choice(tips)
  #remove tip from list to avoid repeating the same tip
  tips.remove(info)
  return info


# ____________________Function: User wants a resource____________________
def resource():
    print("")
    print('Can you please tell me what city you live in?')
    city=input()
    city = city.lower()
    cities(city)
# ___________________Function: Resources for home owners_________________________
def home_owner():
  print('\nDo you own your home?: [y/n]')
  own = input()
  if 'y' in own.lower():
    print("\nYou may qualify for one of the following subsidies. \nThis means the government financially helps you make energy efficient improvements to your home")
    print("Visit: https://www.hieropgewekt.nl/energie-besparen/zelf-energie-besparen/subsidies-en-leningen-voor-isolatie-en-aardgasvrij-wonen#isde for more information and to sign up now!")
    print("More information on how to qualify or apply can be found here: https://mijn.rvo.nl/subsidie-energiebesparing-eigen-huis-verenigingen#")
  if 'n' in own.lower():
      resource()


#__________________________cities options _________________________

def cities(city):
  if 'arnhem' in city:
    print("\nhttps://www.energiebanknederland.nl/  provides free energy coaches and bill pay assistance! Apply for Energiebank Arnhem here: https://energiebankregioarnhem.nl/huishoudens/aanmelden/")
  elif 'the hague' in city:
    print("\nhttps://www.energiebanknederland.nl/ provides free energy coaches and bill pay assistance! Apply for Energiebank The Hague here: https://www.energiebanknederland.nl/de-energiebank/energiebank-den-haag You can also email them directly at info@energiebankdenhaag.nl")
  elif 'den haag' in city:
    print("\nhttps://www.energiebanknederland.nl/ provides free energy coaches and bill pay assistance! Apply for Energiebank The Hague here: https://www.energiebanknederland.nl/de-energiebank/energiebank-den-haag You can also email them directly at info@energiebankdenhaag.nl")
  elif 'harlemmermeer'in city:
    print("\nhttps://www.energiebanknederland.nl/ provides free energy coaches and bill pay assistance! Apply for Energiebank Harlemmermeer here: https://www.energiebanknederland.nl/de-energiebank/energiebank-haarlemmermeer You can also email them directly at: welcome@energiebankhaarlemmermeer.nl or if you prefer, you may call them at this number: 023 20 40 187")
  elif 'kampen' in city:
    print("\nhttps://www.energiebanknederland.nl/ provides free energy coaches and bill pay assistance! Apply for Energiebank Kampen here: 'https://www.energiebanknederland.nl/de-energiebank/energiebank-kampen/ You can also email them directly at: welcome@energiebankkampen.nl or if you prefer, you may call them at this number: 06 570 19 558")
  elif 'rotterdam' in city:
    print("\nhttps://www.energiebanknederland.nl/  provides free energy coaches and bill pay assistance! Apply for Energiebank Rotterdam here: https://www.energiebanknederland.nl/ontvang-energie/aanmelden-rotterdam/ You can also email them directly at: rotterdam@energiebanknederland.nl or if you prefer, you may call them at this number: 010 466 67 22")
  elif 'amsterdam' in city:
    print("\nIn Amsterdam, you can get assistance from your Buurtteam or Neighborhood team. To find your team click here: https://www.buurtteamamsterdam.nl/vind-uw-buurtteam/ ")
  elif 'utrecht' in city:
    print("\nFor more information on the counseling services available in Utrecht click here: https://www.utrecht.nl/werk-en-inkomen/hulp-bij-geldzorgen/To sign up by zip code click here: https://www.buurtteamsutrecht.nl/")
  elif 'amstelveen' in city:
    print("\nFor more information on debt counseling in Amstelveen click here: https://www.amstelveen.nl/public-services/publicatie/amstelveenloket-social-counter-at-town-hall_debt-counseling-schuldhulpverlening Or feel free to give them a call at: (020) 540 49 11")
  else:
    print("\nUnfortunately I could not find an energy coach in your city but I did find this:")
    print("The Dutch government has an Emergency Stop Procedure: https://www.government.nl/latest/news/2020/02/04/government-to-prevent-fines-stacking-up-for-people-in-debt to prevent fines and late fees from stacking up.")
    print("For more information call Vota for help at 06-38419806 or click here: https://www.votad.nl/noodknop-voor-mensen-met-schulden-bij-uwv-of-belastingdienst/")



#__________________________disconnection______________________
def disconnection():
    resource = print(" \n\nI'm sorry to hear that you are dealing with this, but don't worry " +name+ ", I will make sure to keep you safe from electricity disconnection.\n The Dutch Government has a policy in place that protects households from being disconnected due to failure to pay energy bills. It is actually against the law for your energy company to shutoff your power in the Winter months\n \nTo view this policy in Dutch click here: https://wetten.overheid.nl/BWBR0030164/2018-05-01 For an explanation in English click here: https://www.energypoverty.eu/measure-policy/disconnection-protection-households\n")
    return resource
  


#_______________________sentiment analysis____________________

def sentiment():
    ask = print('\n' + name + ", how are you feeling about your energy bill?")
    feeling = input()
    blob=TextBlob(feeling)
    if blob.polarity > 0.5:
        print("\nThat's great to hear! ")
    elif blob.polarity > 0.1:
        print("\nThat's not too bad! ")
    elif blob.polarity < -0.5:
        print("\nOh no, I'm really sorry to hear that :( maybe I can help! ")
    elif blob.polarity < -0.1:
        print("\nI'm sorry to hear this, I know it can be a really stressful process but I am here to help")
    else:
        print('\nTry not to worry! It is important to remember that changing your energy consumption behavior has the potential to reduce your energy usage by 22-27%')

#________________________________________ Intent Recognition functions ________________________________________ 
def function_for_tips():
    print("\nI think I can help you with a helpful energy saving tip like this:")
    print(randomTips())
    
def function_for_resource():
    print("\n I think I can help by connecting you with a resource in your city")
    home_owner()
    
    
def function_for_disconnection():
    disconnection()
    

mappings = {'tips' : function_for_tips, 'resource' : function_for_resource, 'disconnection' : function_for_disconnection}

assistant = GenericAssistant('intents.json', intent_methods=mappings ,model_name="test_model")
assistant.train_model()
assistant.save_model()

#_______________________________________________________ CONVERSATION BEGINS ____________________________________

#1 request users' name

print("")
print("Hello, what's your name?!")
name = input()


#2 Bot intro
print('')
print('Hi ' + name +', my name is Buddy, & I am here to help you manage your energy costs :)')
print('How are you feeling today?')
mood=input()


#3 sentiment analysis
blob=TextBlob(mood)
if blob.polarity > 0.1:
  print("")
  print("I'm happy to hear this! Let's get started, shall we?")
elif blob.polarity < -0.1:
  print("")
  print("I'm sorry to hear this :( maybe there is something I can do!")
else:
  print("")
  print("That's not too bad, let's get started!")

#4 Bot recognizes user input
offer_help = input("\n How can I help you today? ")
assistant.request(offer_help)
pause=input()

#5 User sentiment check in 
sentiment()

#6 continue offering help until the user is done
while True:
    ask = input("\nIs there anything else I can help you with?: [y/n]")
    if 'y' in ask.lower():
        message = input("\nHow can I help you? ")
        assistant.request(message)
    if 'n' in ask.lower():
        print("\nIt was really nice talking with you today "+ name + "! \nDid you find the conversation helpful?")
        helpful=input()
        #sentiment analysis
        blob=TextBlob(helpful)
        if blob.polarity > 0.2:
            print("\n I'm happy to hear this! Come back anytime :)")
        elif blob.polarity < -0.1:
            print("\n I'm sorry to hear this :( why don't we see how I can help you?")
        else:
            print("Okay, that's not too bad. I am improving everyday so please feel free to chat with me another time :)")
        sys.exit()

