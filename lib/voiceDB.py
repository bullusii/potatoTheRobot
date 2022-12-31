## THIS LIB WILL HANDLE ALL THE CONNECTIONS WITH VOICE DB
import sqlite3
from datetime import datetime

class theVoiceDB:
    def __init__(self, config, debug):
        self.db = config['VOICE_DB_PATH'] + '/' + config['VOICE_DB_NAME']
        self.table = config['VOICE_DB_TABLE']
        self.scheduleTable = config['schedule_db_table']
        self.debug = debug

        try:
            self.con = sqlite3.connect(self.db)
            self.cur = self.con.cursor()
        except:
            print("Could not connect to DB at: " + self.db + " ON Table: " + self.table)
            exit()

    ## RETURNS FILE IF IT EXISTS
    def get_voice_data(self,text, type, data):
        returnData = None
        try:
            if type == 'title' or type == 'text':
                query = "SELECT " + data + "  FROM " + self.table + " WHERE " + type + " = '" + text.lower() + "'"
                print("QUERYING : " + query) if self.debug == 2 else None
            else:
                print("ERROR: bad type passed: " + type + " OR data: " + data)

            result = self.cur.execute(query)
            returnData = result.fetchone()[0]
            if self.debug == 1:
                print(returnData)
            return returnData
        except:
            print("WARN: Select query returned 0 results") if self.debug == 1 else None
            return returnData

    def insert_sound_file(self,clip_id, body, title):
        try:
            query = "INSERT INTO " + self.table + " VALUES ('" + clip_id + "','" + body.lower() + "','TBD','TBD','" + title + "')"
            self.cur.execute(query)
            self.con.commit()
            print("Audio Content Added to VoiceDB")
        except:
            print("ERROR: Audio Content was not INSERTED to DB")

    def update_sound(self,s3_path, clip_local_path, clip_id):
        try:
            self.cur.execute("UPDATE clips SET s3_path = ?, local_path = ? WHERE uuid = ?", (s3_path, clip_local_path, clip_id))
            self.con.commit()
            print("Updated Content")
        except:
            print("ERROR: Audio Content was not UPDATED to DB")


    ## Checks if there are dates in the schedule table
    def getScheduledEvent(self):
        date = datetime.now()
        full_date = str(date.month) + '-' + str(date.day) + '-' + str(date.year)
        try:
            query = "SELECT id, file_path FROM " + self.scheduleTable + " WHERE playDate = '" + full_date + "' AND playHour=" + str(date.hour) + " AND playMin=" + str(date.minute) + " AND wasPlayed=0"
            result = self.cur.execute(query)
            print("QUERYING : " + query) if self.debug == 2 else None
            id, file_path = result.fetchone()
            return id, file_path
        except:
            return None

    def updateScheduledEvent(self,id):
        try:
            query = "UPDATE " + self.scheduleTable + " SET wasPlayed=1 WHERE id=" + str(id)
            print("UPDATING DB: " + query) if self.debug == 1 else None
            self.cur.execute(query)
            self.con.commit()
        except:
            print("ERROR: scheduled event not updated as played")

    def insertScheduledEvent(self, date, file, message):
        try:
            full_date = str(date.month) + '-' + str(date.day) + '-' + str(date.year)
            query = "INSERT INTO " + self.scheduleTable + " (playDate, playHour, playMin,file_path,message,wasPlayed) VALUES('" + full_date + "'," + str(date.hour) + "," + str(date.minute) + ",'" + file + "','" + message + "',0)"
            print("INSERTING DB: " + query) if self.debug == 1 else None
            self.cur.execute(query)
            self.con.commit()
            print("SUCCESS: Event Scheduled!")
        except Exception:
            print(Exception)
            print("ERROR: scheduled event not INSERTED as played")

    def get_all_sayings(self):
        try:
            query = "SELECT text, local_path FROM " + self.table + " WHERE local_path != 'TBD'"
            result = self.cur.execute(query)
            print("QUERYING : " + query) if self.debug == 1 else None
            return result.fetchall()
        except Exception:
            print ("ERROR: No results to return fetch all.")
            print(Exception)

    def get_all_events(self):
        try:
            query = "SELECT playDate, playHour, playMin, message FROM " + self.scheduleTable + " WHERE wasPlayed=0 ORDER BY playDate,playHour,playMin"
            result = self.cur.execute(query)
            print("QUERYING : " + query) if self.debug == 1 else None
            return result.fetchall()
        except Exception:
            print ("ERROR: No results to return all events.")
            print(Exception)
