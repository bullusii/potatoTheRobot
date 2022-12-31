
##THIS DOESNT WORK AS an EXECUTIBLE
import sqlite3
con = sqlite3.connect("voice.db")
cur = con.cursor()
cur.execute("CREATE TABLE clips(uuid, words, s3_path, local_path, title)")


## CREATE TABLE scheduled(id INTEGER PRIMARY KEY AUTOINCREMENT, playDate, playHour, playMin,file_path, message, wasPlayed);
