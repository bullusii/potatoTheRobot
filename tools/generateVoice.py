#!/usr/bin/python
import sqlite3
import json
from resemble import Resemble

## from app.resemble.ai  >> gererates voices

token = 'Xo5AyVhdinf6tS43SbyEswtt'
project_uuid = '308a30f0'
voice_uuid = '0a947b50'
precision = 'PCM_16'
sample_rate = 22050
output_format = 'mp3'
callback_uri = 'https://mvx4thwh34.execute-api.us-east-1.amazonaws.com/Prod/skelly/voiceapi/'
skelly_api_key = "fjdlksajfi4ut840ugjvosnf9u40j3f3ml3co30489jojd"
title = None
include_timestamps = None
is_public = None
is_archived = None

Resemble.api_key(token)

demo =  "I am the coolest Skelleton"
clue1 = "Ahhh, you have begun your scavenger hunt for Christmas. Clue number one. Look for the clue number two by searching for the bag with the fluffiest pokemons. Scary Christmas."
## clue 2 with build a bear 1
clue2 = "Good job the Wendel. Finding is the hardest game. This is just the beginning, ha ha ha. The next clue can be found where you can find many pika pikas on leather."
## clue 3 with build a bear 2
clue3 = "Now you are heating up. You seem to be getting the hang of this. You are starting to amass some treasure. Find your most expensive thing bearing Karomi and maybe you will find more prizes."
## clue 4 with build a bear 3
clue4 = "On to the next one. I am a treasure hidden deep, in a boot where flowers creep. In a cave covered in cloth, is where this treasure has been lost."
## clue 5 with build a bear 4
clue5 = "Ha ha. The little treasures have been found. Now for the bigger ones. A riddle. shoes whipe on top my head, Chirstmas was the day I dread. I have a puppy I do not treat well, but find my clue or I will not tell."
## clue 6 no treasure but leads to the last in a lunch box with all the boxed lunch gift cards
clue6 = "Wendel, Katara, look at you, you have made it to the final clue. I travel with Katara every day, except the best day of the week. So if it is my treasure that you seek, in a food box you must peak."
## just a cute outro - can add a song too if I have time (probably not)
clue7 = "Congratulations, you have found all my clues... Now, look inside my sack, for the best present off all is waiting for you. Scary Christmas everyone. ho, ho, ho."

## DATA TO PROCESS
body = clue7
title = "clue 7" ## using this because it makes easier codes to read

## Catch bad type
if "'" in body:
    print('Appostrophies do not work currently, rewrite the body')
    exit()


response_raw = Resemble.v2.clips.create_async(
    project_uuid,
    voice_uuid,
    callback_uri,
    body,
    title,
    sample_rate,
    output_format,
    precision,
    include_timestamps,
    is_public,
    is_archived
)

print(response_raw)
clip_id = response_raw['item']['uuid']

## uuid, text, s3_path, local_path
query = "INSERT INTO clips VALUES ('" + clip_id + "','" + body.lower() + "','TBA','TBA','" + title + "')"
con = sqlite3.connect('/home/bullusii/voice.db')
cur = con.cursor()
res = cur.execute(query)
con.commit()
con.close()
