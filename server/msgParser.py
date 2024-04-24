def isNumber(s):
        try:
          float(s)
          return True
        except ValueError:
          return False

# Обработка сообщения от клиента
def parseMsg(msg):
        data = msg.split(",")
        action = data[0].split(' ')[0]
        if not any(action == item for item in ('-post', '-get_by_name','-get_by_phonenumber', '-delete')):
            return {'action': "no action"}
        firstArg = ' '.join(data[0].split(' ')[1:])
        secondArg = ""
        if len(data) > 1:
            secondArg = data[1]
        if action == "-post" and len(data) > 1 and isNumber(secondArg) :
            name = firstArg
            phoneNumber = secondArg.strip()
            note = ""
            if len(data) == 3:
                note = data[2].strip()
            return {'action': action, 'name': name, 'phonenumber': phoneNumber, 'note': note}
        elif action == "-delete" and len(data) == 1:
                name = firstArg
                return {'action': action, 'name': name}
        elif action == "-get_by_phonenumber" and len(data) == 1 and isNumber(firstArg):
                phoneNumber = firstArg
                return {'action': action, 'phonenumber': phoneNumber}
        elif action == "-get_by_name" and len(data) == 1:
                name = firstArg
                return {'action': action, 'name': name}
        else:
            return {'action': "no action"}