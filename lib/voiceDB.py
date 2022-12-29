## THIS LIB WILL HANDLE ALL THE CONNECTIONS WITH VOICE DB
import sqlite3

class theVoiceDB:
    def __init__(self, config, debug):
        self.db = config['VOICE_DB_PATH'] + '/' + config['VOICE_DB_NAME']
        self.table = config['VOICE_DB_TABLE']
        self.debug = debug

        try:
            self.con = sqlite3.connect(self.db)
            self.cur = self.con.cursor()
        except:
            print("Could not connect to DB at: " + self.db + " ON Table: " + self.table)
            exit()

    ## RETURNS FILE IF IT EXISTS
    def get_local_sound_file(self,text, type):
        localSoundFilePath = None
        try:
            if type == 'title' or type == 'text':
                query = "SELECT local_path FROM " + self.table + " WHERE " + type + " = '" + text.lower() + "'"
                if self.debug == 1:
                    print("QUERYING : " + query)
            else:
                print("ERROR: bad type passed: " + type)

            result = self.cur.execute(query)
            localSoundFilePath = result.fetchone()[0]
            if self.debug == 1:
                print(localSoundFilePath)
            return localSoundFilePath
        except:
            print("ERROR: Executing Query to sqlite3")
            return localSoundFilePath

    def insert_sound_file(self,clip_id, body, title):
        try:
            query = "INSERT INTO " + self.table + " VALUES ('" + clip_id + "','" + body.lower() + "','TBA','TBA','" + title + "')"
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
