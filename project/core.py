
import random
from adapt.intent import IntentBuilder
from adapt.engine import IntentDeterminationEngine

symptoms = {"fever":"","cold":"","bodypain":"","tired":"","headache":"",
            "vomitation":"","stomachpain":""}

engine = IntentDeterminationEngine()

symptoms_word=["do you have any symptoms like", "do you feel","do you have", "are you feeling", "ary you having"]
symptoms_word2=["do you have any other symptoms", "nothing else right","everything lese is okay right", "anything else"]

greeting_word = ['hi','hello','hii', 'Hello','Howdy']
greeting_response = ['hi, how are you','hello, any physical illness','hii, nice to hear from you', 'Hello','Howdy', "Hi","hello"]

greeting_word2 = ['thanks','thanks you','okay', 'nice']
greeting_response2 = ['You are welcome','Happy to help','Have a nice day', 'get well soon']



for word in greeting_word:
    engine.register_entity(word, "greeting")
intent1 = IntentBuilder("greetingIntent")\
    .require("greeting")\
    .build()
engine.register_intent_parser(intent1)
for word in greeting_word2:
    engine.register_entity(word, "greeting2")
intent2 = IntentBuilder("greeting2Intent")\
    .require("greeting2")\
    .build()
engine.register_intent_parser(intent2)

fever_word = ['temperature','fever','hot body', 'body hot','heat']
for word in fever_word:
    engine.register_entity(word, "fever")
intentfeaver = IntentBuilder("feverIntent")\
    .require("fever")\
    .build()
engine.register_intent_parser(intentfeaver)

cold_word = ['cold','chill','freezing', 'chill']
for word in cold_word:
    engine.register_entity(word, "cold")
intentcold = IntentBuilder("coldIntent")\
    .require("cold")\
    .build()
engine.register_intent_parser(intentcold)

bodypain_word = ['body pain','body paining','paining', 'body','pain','bodypain']
for word in bodypain_word:
    engine.register_entity(word, "bodypain")
intentbodypain = IntentBuilder("bodypainIntent")\
    .require("bodypain")\
    .build()
engine.register_intent_parser(intentbodypain)

tired_word = ['tired','tiredness','dull', 'energy','drained']
for word in tired_word:
    engine.register_entity(word, "tired")
intenttired = IntentBuilder("tiredIntent")\
    .require("tired")\
    .build()
engine.register_intent_parser(intenttired)

headache_word = ['head','ache','head ache', 'headache']
for word in headache_word:
    engine.register_entity(word, "headache")
intentheadache = IntentBuilder("headacheIntent")\
    .require("headache")\
    .build()
engine.register_intent_parser(intentheadache)

vomitation_word = ['vomit','digestion','vomitation', 'food','vomitted']
for word in vomitation_word:
    engine.register_entity(word, "vomitation")
intentvomitation = IntentBuilder("vomitationIntent")\
    .require("vomitation")\
    .build()
engine.register_intent_parser(intentvomitation)

stomachpain_word = ['stomach','stomachpain','indigestion', 'digestion', 'stomach pain']
for word in stomachpain_word:
    engine.register_entity(word, "stomachpain")
intentstomachpain = IntentBuilder("stomachpainIntent")\
    .require("stomachpain")\
    .build()
engine.register_intent_parser(intentstomachpain)





def clear_symptoms():
    global symptoms
    symptoms = {"fever":"","cold":"","bodypain":"","tired":"","headache":"",
            "vomitation":"","stomachpain":"","drycough":"","sneeze":""}

def process(message,previous_msg):
    intent=[]
    res = "i couldnt get you... please explain your medical symptoms..."
    print("in processing...",message,)
    
    for intent_detected in engine.determine_intent(message):
        print ("messages",message,"\ndetected:",intent_detected)
        if intent_detected['intent_type'] == "greetingIntent":
             res = greeting_response[random.randint(0,len(greeting_response)-1)]
             data =  {'message': 'Created', 'code': 'SUCCESS','res':res}
             return data
        if intent_detected['intent_type'] == "greeting2Intent":
             res = greeting_response2[random.randint(0,len(greeting_response2)-1)]
             data =  {'message': 'Created', 'code': 'SUCCESS','res':res}
             return data
        if intent_detected['intent_type'] == "feverIntent":
             symptoms["fever"]="yes"
        if intent_detected['intent_type'] == "coldIntent":
             symptoms["cold"]="yes"
        if intent_detected['intent_type'] == "bodypainIntent":
             symptoms["bodypain"]="yes"
        if intent_detected['intent_type'] == "tiredIntent":
             symptoms["tired"]="yes"
        if intent_detected['intent_type'] == "headacheIntent":
             symptoms["headache"]="yes"
        if intent_detected['intent_type'] == "vomitationIntent":
             symptoms["vomitation"]="yes"
        if intent_detected['intent_type'] == "stomachpainIntent":
             symptoms["stomachpain"]="yes"

    
    print("Symptoms:",symptoms,"\n")
    
    if "yes" in message or "hmm" in message or "yeah" in message:
        for intent_detected in engine.determine_intent(previous_msg):
            print ("messages",message,"\ndetected:",intent_detected)
            if intent_detected['intent_type'] == "feverIntent":
                 symptoms["fever"]="yes"
            if intent_detected['intent_type'] == "coldIntent":
                 symptoms["cold"]="yes"
            if intent_detected['intent_type'] == "bodypainIntent":
                 symptoms["bodypain"]="yes"
            if intent_detected['intent_type'] == "tiredIntent":
                 symptoms["tired"]="yes"
            if intent_detected['intent_type'] == "headacheIntent":
                 symptoms["headache"]="yes"
            if intent_detected['intent_type'] == "vomitationIntent":
                 symptoms["vomitation"]="yes"
            if intent_detected['intent_type'] == "stomachpainIntent":
                 symptoms["stomachpain"]="yes"


    if "no" in message:
        for intent_detected in engine.determine_intent(previous_msg):
            print ("messages",message,"\ndetected:",intent_detected)
            if intent_detected['intent_type'] == "feverIntent":
                 symptoms["fever"]="no"
            if intent_detected['intent_type'] == "coldIntent":
                 symptoms["cold"]="no"
            if intent_detected['intent_type'] == "bodypainIntent":
                 symptoms["bodypain"]="no"
            if intent_detected['intent_type'] == "tiredIntent":
                 symptoms["tired"]="no"
            if intent_detected['intent_type'] == "headacheIntent":
                 symptoms["headache"]="no"
            if intent_detected['intent_type'] == "vomitationIntent":
                 symptoms["vomitation"]="no"
            if intent_detected['intent_type'] == "stomachpainIntent":
                 symptoms["stomachpain"]="no"

    if symptoms["fever"] == "yes" and symptoms["cold"] == "yes" and symptoms["bodypain"] == "yes" and symptoms["tired"] == "yes":
       res = "Please take some rest and hava a mild medication such as Dolo 500 in morning and evening, it helps to reduce fever and cold with body pain, if persists please consult a doctor" 
       clear_symptoms()
       data =  {'message': 'Created', 'code': 'SUCCESS','res':res}
       return data
    if symptoms["fever"] == "yes" and symptoms["cold"] == "no" and symptoms["bodypain"] == "no" and symptoms["tired"] == "yes":
       res = "Please take some rest and take Dolo 500 in morning and evening, it helps to reduce fever if persists please consult a doctor, dont take feaver as light, check doctor as soon as possible" 
       clear_symptoms()
       data =  {'message': 'Created', 'code': 'SUCCESS','res':res}
       return data
    if symptoms["fever"] == "no" and symptoms["cold"] == "yes" and symptoms["bodypain"] == "no" and symptoms["tired"] == "yes":
       res = "Please take some rest and take Dolo 500 post haveing some food, if persists please consult a doctor " 
       clear_symptoms()
       data =  {'message': 'Created', 'code': 'SUCCESS','res':res}
       return data
    if symptoms["vomitation"] == "yes" or symptoms["vomitation"] == "yes" :
       res = "please take light food and get some rest, take Dolo 500 post haveing little food, if persists please consult a doctor " 
       clear_symptoms()
       data =  {'message': 'Created', 'code': 'SUCCESS','res':res}
       return data
    if symptoms["headache"] == "yes":
       res = "Please take some rest have a quick sleep,after waking up if persists please consult a doctor " 
       clear_symptoms()
       data =  {'message': 'Created', 'code': 'SUCCESS','res':res}
       return data
    if symptoms["fever"] == "no" and symptoms["cold"] == "no" and symptoms["bodypain"] == "no" and symptoms["tired"] == "no" and symptoms["headache"] == "no":
       res = "You are a healthy person... Have a great day..." 
       clear_symptoms()
       data =  {'message': 'Created', 'code': 'SUCCESS','res':res}
       return data

    for key in symptoms:
        if symptoms[key]=="":
            list2=[(symptoms_word[random.randint(0,len(symptoms_word)-1)] + " " +key),(symptoms_word2[random.randint(0,len(symptoms_word2)-1)])]
            res = random.choice(list2)
            break
    data =  {'message': 'Created', 'code': 'SUCCESS','res':res}
    return data






