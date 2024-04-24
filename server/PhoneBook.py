import sqlite3

class PhoneBook:
    def __init__(self, dbName):
        self.dbName = dbName
        
    def addRecord(self, name, phoneNumber, note):
        # Добавление записи в телефонную книгу
        with sqlite3.connect(self.dbName) as conn:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS PhoneBook (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                phonenumber TEXT NOT NULL,
                note TEXT
                )
                ''')
                phoneNumber = str(phoneNumber) 
                cursor.execute('INSERT INTO PhoneBook (name, phonenumber, note) VALUES (?, ?, ?)', (name, phoneNumber, note))
            except sqlite3.DatabaseError as err:       
                return err
            else:
                conn.commit()


    def deleteRecord(self, name):
        # Удаление записи из телефонной книги
        with sqlite3.connect(self.dbName) as conn:
            try:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM PhoneBook WHERE name = ?', (name,))
            except sqlite3.DatabaseError as err:       
                return err
            else:
                conn.commit()



    def getRecordByName(self, name):
        # Получение записи из телефонной книги по имени
        with sqlite3.connect(self.dbName) as conn:
            try:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM PhoneBook WHERE name = ?', (name,))
                result = cursor.fetchone()
            except sqlite3.DatabaseError as err:       
                return "", err
            else:
                conn.commit()
                if not result:
                  return "", None
                return ' '.join(map(str, result[1:])), None

            
    def getRecordByPhoneNumber(self, phoneNumber):
        # Получение записи из телефонной книги по номеру телефона
        with sqlite3.connect(self.dbName) as conn:
            try:
                cursor = conn.cursor()
                str(phoneNumber)
                cursor.execute('SELECT * FROM PhoneBook WHERE phonenumber = ?', (phoneNumber,))
                result = cursor.fetchone()
                print(result)
            except sqlite3.DatabaseError as err:       
                return "", err
            else:
                conn.commit()
                if not result:
                  return "", None 
                return ' '.join(map(str, result[1:])), None
    
    