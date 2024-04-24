from PhoneBook import *
import asyncio
import msgParser
import socket

def addRecord(name, phoneNumber, note):
        # Добавление записи в телефонную книгу
        phoneBook = PhoneBook("PhoneBookRecords.db")
        err = phoneBook.addRecord(name, phoneNumber, note)
        if not err:
            return "Record added successfully!"
        else:
            return str(err)

def deleteRecord(name):
        # Удаление записи из телефонной книги
        phoneBook = PhoneBook("PhoneBookRecords.db")
        err = phoneBook.deleteRecord(name)
        if not err:
            return f'Record with name {name} deleted successfully!'
        else:
            return str(err)
        
def getRecordByName(name):
        # Получение записи из телефонной книги по имени
        phoneBook = PhoneBook("PhoneBookRecords.db")
        res, err = phoneBook.getRecordByName(name)
        if res and not err:
            return res
        elif not res:
            return f'Record with name {name} not found!'
        else :
            return str(err)

def getRecordByPhone(phoneNumber):
        # Получение записи из телефонной книги по номеру телефона
        phoneBook = PhoneBook("PhoneBookRecords.db")
        res, err = phoneBook.getRecordByPhoneNumber(phoneNumber)
        if res and not err:
            return res
        elif not res:
            return f'Record with phonenumber {phoneNumber} not found!'
        else :
            return str(err)


async def handle_connection(reader, writer):
    addr = writer.get_extra_info("peername")
    print(f'[CONNECTED BY {addr}]')
    while True:
        try:
            # Получение сообщение от клиента
            try:
                msg = await reader.read(1024) 
            except ConnectionError:
                print(f'[CLIENT SUDDENLY CLOSED WHILE RECEIVING FROM {addr}]')
                break
            print(f"Received {msg} from: {addr}")
            if not msg:
                break
            # Обработка сообщения
            if msg == b"close":
                break
            
            data = msgParser.parseMsg(msg.decode('utf-8'))
            action = data['action']
               
            if action == "-post":
                name = data['name']
                phoneNumber = data['phonenumber']
                note = data['note']
                response = addRecord(name, phoneNumber, note)
            elif action == "-delete":
                name = data['name']
                response = deleteRecord(name)
            elif action == "-get_by_phonenumber":
                phoneNumber = data['phonenumber']
                response = getRecordByPhone(phoneNumber)
            elif action == "-get_by_name":
                name = data['name']
                response = getRecordByName(name)
            else:
                response = "Invalid request"

            # Отправка сообщения клиенту
            print(f"Send: {response} to: {addr}")
            try:
                writer.write(response.encode("utf-8"))  
                await writer.drain()
            except ConnectionError:
                print("[CLIENT SUDDENLY CLOSED, CANNOT SEND]")
                break
        except KeyboardInterrupt:
            global exception_task
            exception_task = asyncio.current_task()
            raise
        
    writer.close()
    print(f'[DISSCONNECTED BY {addr}]')


async def main(host, port):
    server = await asyncio.start_server(handle_connection, host, port)
    print(f"[LISTENNING] Server listening on {host}:{port}")
    async with server:
        await server.serve_forever()
   
      
HOST = socket.gethostbyname(socket.gethostname()) 
PORT = 5050  

if __name__ == "__main__":
    asyncio.run(main(HOST, PORT))

