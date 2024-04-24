import socket
import argparse 

def parseArquments():
      try:
         parser = argparse.ArgumentParser(description='Phonebook app') 
    
         parser.add_argument('ip', type=str, help='server IP address running on')
         parser.add_argument('port', type=int, help='server port running on')

         given_args = parser.parse_args() 
         ip = given_args.ip
         port = given_args.port 
      except Exception as e:
         print(str(e))
         exit(-1)

      return (ip, port)

startMsg = """
    Список команд:
    -post <"имя фамилия отчество">, <"номер телефона">, <"записка">
    -get_by_name <"имя фамилия отчество">
    -get_by_phonenumber <"номер телефона">
    -delete <"имя фамилия отчество">
    """ 

if __name__ == "__main__":
    serverAdress = parseArquments()
    print(startMsg)
    print("[CREATE CLIENT]")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Соединение с сервером
        sock.connect(serverAdress)
        print("[CLIENT CONNECTED]")
        while True:
            # Получение данных от пользователя
            try:
                data = input("Enter request:")
            except KeyboardInterrupt:
                print('[CLIENT STOPPED]')
                break
            # Отправка сообщения
            data_bytes = data.encode()
            sock.sendall(data_bytes)
            # Получение ответа от сервера
            data_bytes = sock.recv(1024)
            data = data_bytes.decode()
            print("Received:", repr(data))
            if not data:
                print("[CLOSED BY SERVER]")
                break
        sock.close()
        print("[CLIENT DESSCONNECTED]")



