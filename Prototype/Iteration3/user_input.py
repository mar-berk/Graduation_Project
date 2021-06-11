import pandas as pd
import json
import string
import csv


#Add the inputs from initial data collection to  user_input.csv
'''
sample_data = {'input': ['lower bill','how can i reduce my energy use','hi im looking for ways to reduce my energy usage','hi im looking for ways to reduce my energy uses','what small changes can i make to my energy use to make my energy bill lower','is there a way i can reduce my energy bill','how can i lower my bill','how to conserve energy use','i need tips to reduce my energy bill','tips to reduce my energy bill','what can I do to lower my energy bill','my energy bill is rather high can you help','reduce power costs','tips to reduce energy bill','what are some ways i can reduce my energy bill','ways to reduce my bill or ways to reduce my consumption','i cannot afford to pay my bill this month what solutions do you have for me','can you help me manage my debt', 'can you show me a resource','can you show me an energy coach', 'i need somebody to help me''is there anyone that can come to my home and help me', 'is there anyone who can come help me''do you have any additional resources that i might be missing','what resources are available to me to lower my bill','help avoiding electricity shutoff','how to pay bill later but keep electricity on','how to keep electricity on if i cant pay','will my electricity stay on if i cant pay my bill','how can i avoid electricity shutoff', 'how can i avoid my electricity being shut off', 'how do i prevent disconnection', 'how do i prevent shutoff', 'is there a way i can pay the bill over an extended period of time', 'im about to get my electricity shutoff what should i do immediately', 'i am currenctly facing the threat of electricity shutoff and am looking to avoid that by any means possible what should i do','how can i keep my electricity from being shutoff', 'how can i keep my electricity from being disconnected'],
        'topic': ['tips','tips','tips','tips','tips','tips','tips','tips','tips','tips','tips','tips','tips','tips','tips','tips','resource','resource','resource','resource','resource','resource','resource','disconnection','disconnection','disconnection','disconnection','disconnection','disconnection','disconnection','disconnection','disconnection','disconnection','disconnection','disconnection','disconnection']
        }
sample_dataframe = pd.DataFrame(data=sample_data)
sample_dataframe.to_csv ('user_input.csv', index = False, header=True)

#This section is commented out now so as not to override the additional inputs that have been added from user testing
print (sample_dataframe)
'''

#Combine user_input.csv with newly collected inputs from survey (input2)
df1 = pd.read_csv("user_input.csv") #This contains user inputs from initial data collection & user testing
df2 = pd.read_csv("input2.csv") #This contains the user inputs from second data collection survey (automatically exported into a csv from google forms)
df = pd.concat([df1, df2], ignore_index=True)

#_______________________________DATA CLEANING_______________________________


#drop the duplicate entries
df = df.drop_duplicates()

#sort the values by topic
df.sort_values(by=['topic'], inplace=True)

#remove capital letters
df['input'] = df['input'].str.lower()

#remove punctuation
def remove_punctuations(text):
        for punctuation in string.punctuation:
                text =text.replace(punctuation,'')
        return text
#apply to the DF
df['input'] = df['input'].apply(remove_punctuations)

#Remove space at the end of the input statements 
df=df.replace(' ,',',',regex=True)

#print(df)

#save the new df to a csv
df.to_csv ('training_data.csv', index = False, header=True)
print(df)

'''
#Save new df as JSON
topic = df['topic']
message = df['input']
intents_2 =[]
data= {"tag":topic, "patterns": message}
intents_2.append(data)

with open("intents2.json",'w')as outfile:
        json.dump(intents_2,outfile)

'''

#df.to_json('intents2.json', orient='records', lines=True)

