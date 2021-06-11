import random
from textblob import TextBlob
import sys
import pandas as pd
import string


#load the inputs csv containing inputs from data collection
df = pd.read_csv("training_data.csv")

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
# ______________________ Bot identifies topic from user input_________________
def identify():
  question = '\nWhat topic did you want help with?: [a/b/c/d]\n'
  optionA = 'A. energy saving tips\n'
  optionB = 'B. help sign you up for programs & subsidies you qualify for\n'
  optionC = 'C. disconnection protection resources\n'
  optionD = 'D. other'
  print('\n',question,optionA,optionB,optionC,optionD )
  
#_____________________ Bot offers assistance_____________________________
def help_request():
  question = 'Please let me know how I can help you next by selecting one of the options: [a/b/c]\n'
  optionA = 'A. energy saving tips\n'
  optionB = 'B. sign me up for programs & subsidies\n'
  optionC = 'C. disconnection protection resources\n '
  print('\n', question, optionA, optionB, optionC )

# ____________________User wants a resource____________________
def resource():
    print("")
    print('I understand that you would like help signing up for programs and subsidies you qualify for')
    print('Can you please tell me what city you live in?')
    city=input()
    city = city.lower()
    cities(city)
# ___________________Resources for home owners_________________________
def home_owner():
  print('Do you own your home?: [y/n]')
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
    resource = print(" \nI'm sorry to hear that you are struggling to pay your energy bill this month, but don't worry " +name+ ", I will make sure we keep you safe from electricity disconnection.\n \nThe Dutch Government has a policy in place that protects households from being disconnected due to failure to pay energy bills. It is actually against the law for your energy company to shutoff your power in the Winter months\n \nTo view this policy in Dutch click here: https://wetten.overheid.nl/BWBR0030164/2018-05-01 For an explanation in English click here: https://www.energypoverty.eu/measure-policy/disconnection-protection-households\n")
    return resource
  


#_______________________sentiment analysis____________________

def sentiment():
    ask = print('\n' + name + ", how are you feeling about your energy bill?")
    feeling = input()
    blob=TextBlob(feeling)
    if blob.polarity > 0.5:
        print("\nThat's great to hear! ")
    if blob.polarity > 0.1:
        print("\nThat's not too bad! ")
    elif blob.polarity < -0.5:
        print("\nOh no, I'm really sorry to hear that :( maybe I can help! ")
    elif blob.polarity < -0.1:
        print("\nI'm sorry to hear this, I know it can be a really stressful process but I am here to help")
    else:
        print('\nIt is important to remember that changing your energy consumption behavior has the potential to reduce your energy usage by 22-27%')



#_________________________________________ CONVERSATION BEGINS __________________________

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
  print("I'm sorry to hear this :( why don't we see how I can help you?")

intro=input()



#4 Bot recognizes user input

#get user input 
user_input = input("\nHow can I help you today? ")
#remove capital letters
user_input = user_input.lower()
#remove punctuation
punctuation = "?.,'!@+/"
for c in user_input:
  if c in punctuation:
    user_input = user_input.replace(c,"")


  
#find topic from user input
def find_topic():
  match = df.loc[df['input']==user_input,'topic']
  match = match.reset_index()
  topic = match['topic'][0]

  if 'tips' in topic:
    print("\nI think I can help you with a helpful energy saving tip like this:")
    print(randomTips())
  elif 'Disconnection' in topic:
    disconnection()
  elif 'resource' in topic:
    print('\n I understand that you would like help signing up for programs and subsidies you qualify for')
    print('Can you please tell me what city you live in?')
    city=input()
    city = city.lower()
    cities(city)


#See if the users input is in the csv, if not offer help
if user_input in df['input'].values:
  find_topic()
  wait=input()
else:
  #Add the users input to the training_data.csv
  print("\n I'm sorry, I didn't quite understand that")
  identify()
  y=input()
  if 'a' in y.lower():
    #Make a list to append the new input and new topic to the csv
    new_input={'input': [user_input],
          'topic':['tips']
    }
    df_new = pd.DataFrame(data=new_input)
    df = pd.concat([df,df_new], axis=0)
    df.index = range(len(df.index))
    df.to_csv ('training_data.csv', index = False, header=True)
    print(randomTips())
  elif 'b' in y.lower():
    new_input2={'input': [user_input],
          'topic':['resource']
    }
    df_new2 = pd.DataFrame(data=new_input2)
    df = pd.concat([df,df_new2], axis=0)
    df.index = range(len(df.index))
    df.to_csv ('training_data.csv', index = False, header=True)
    home_owner()
  elif 'c' in y.lower():
    new_input3={'input': [user_input],
          'topic':['disconnection']
    }
    df_new3 = pd.DataFrame(data=new_input3)
    df = pd.concat([df,df_new3], axis=0)
    df.index = range(len(df.index))
    df.to_csv ('training_data.csv', index = False, header=True)
    disconnection()
  elif 'd' in y.lower():
    print("\noops, that's new for me. I'm always learning so maybe next time I can help with that")
    print("For now, why don't we try one of the options in the list?")
    #create a new topic in the list to identify topics that need to be added
    new_input4={'input': [user_input],
          'topic':['other']
    }
    df_new4 = pd.DataFrame(data=new_input4)
    df = pd.concat([df,df_new4], axis=0)
    df.index = range(len(df.index))
    df.to_csv ('training_data.csv', index = False, header=True)
  pause = input()



	

#5 Bot offers additional assistance
help_request()
x = input()

#Conditions for bot assistance 
if 'a' in x.lower():
    print("")
    print("I understand you want an energy tip, that's great! \nDid you know that changing your energy consumption behavior has the potential to reduce your energy usage by 22-27%")
    behavior=input()
    if 'y' in behavior.lower():
        print("\nThat's awesome!! Make sure to tell your family members and housemates as well so you can achieve the best energy & money saving results! Okay here is your energy tip: ")
        print(randomTips())
    elif 'n' in behavior.lower():
        print("\nDon't worry if you didn't know this, that is what I am here for :) ")
    else:
        print(randomTips())

elif 'b' in x.lower():
    home_owner()
elif 'c' in x.lower():
    disconnection()
ans = input()


#4 User sentiment check in 
sentiment()

#5 Continuing the conversation until the user is finished

while True:
    ask = input("\nIs there anything else I can help you with?: [y/n]")
    if 'y' in ask.lower():
        help_request()
        option = input()
        if 'a' in option.lower():
            print(randomTips())
        elif 'b' in option.lower():
            print('\n I understand that you would like help signing up for programs and subsidies you qualify for')
            print('Can you please tell me what city you live in?')
            city=input()
            city = city.lower()
            cities(city)
        elif 'c' in option.lower():
            disconnection()
        ans = input()
    elif 'n' in ask.lower():
        print("\n It was really nice talking with you today "+ name + "! \nDid you find the conversation helpful?")
        helpful=input()
        #sentiment analysis
        blob=TextBlob(helpful)
        if blob.polarity > 0.3:
            print("\n I'm happy to hear this! Come back anytime :)")
        elif blob.polarity < -0.1:
            print("\n I'm sorry to hear this :( why don't we see how I can help you?")
        else:
            print("Okay, that's not too bad. I am improving everyday so please feel free to chat with me another time :)")
        sys.exit()

       

