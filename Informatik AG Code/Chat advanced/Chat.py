import simple_socket, threading, sys, json, time, encrypt
mutex = threading.Lock()

def begr_text():
    """Gibt eine Begrüßungsnachricht im ASCII Stil aus"""
    print("----------Willkommen----------")
    print("----------Version 1.0---------")
    print(r"'/exit' zum Schließen")

def time_conv(timeinsec):
    """konvertiert die Zeit von Sekunden seit 'dem Jahr' in normale Uhrzeit
    """
    realtime = time.localtime(timeinsec)
    minute = realtime[4]
    hour = realtime[3]
    thetime = str(hour) + ":" + str(minute)
    print(thetime)

def connect():
    """returns the server address from the user input
    or returns the standart address
    """
    global serveradr
    serveradr = input("Geben Sie die Adresse ein bzw. s oder h: ")
    if serveradr == "s" or serveradr == "S":
        serveradr = "127.0.0.1"
        server_port = 8888
    elif serveradr == "h":
        serveradr = "h-software.de"
        server_port = 5269
    else:
        server_port = int(input("Geben sie den Port ein: "))
    new_socket = simple_socket.connect_as_client(server_address=serveradr, server_port=server_port)
    return new_socket

def send():
    """sends a message and converts it into json style
    """
    global new_socket, username, mutex              
    encryptor = 26
    login = {
  "nachrichten_id": 2,
  "aktion": "login",
  "sender_name": username,
  "zeitstempel": time.time(),
  "protokoll_version": "0.2"
    }
    json_protocole = json.dumps(login)
    new_socket.send(login)
    for line in sys.stdin:
        if line == "/exit\n":
            logout = {
  "nachrichten_id": 2,
  "aktion": "logout",
  "sender_name": username,
  "zeitstempel": time.time(),
  "protokoll_version": "0.2"
    }
            new_socket.send(logout)
            new_socket.close()
            break
        elif line == "\n":
            pass
        else:
            line = encrypt.encrypt_normal(line, encryptor)
            message = {
  "nachrichten_id": 1,
  "text": line,
  "text_länge": len(line),
  "verschlüsselung": 
  {
    "algorithmus": "caesar",
    "parameter": [encryptor],
    "verschlüsselte parameter": []
  },
  "sender_name": username,
  "zeitstempel": time.time(),
  "protokoll_verion": "0.2"
}
            json_protocole = json.dumps(message)
            new_socket.send(json_protocole)
    return

def get_message(serveraddress):
    """tries to recieve theoretically incoming messages
    """
    global new_socket, mutex
    while True:
        json_message = new_socket.receive()
        json_message = json.loads(json_message)
        if json_message == None:
            pass
        elif json_message["nachrichten_id"] == 1:
            message = json_message["text"]
            shifting_nr = json_message["verschlüsselung"]["parameter"]
            integer = 0
            for i in range(0):
                integer = shifting_nr[0]
            shifting_nr = integer
            message = encrypt.decrypt_normal(message, shifting_nr)
            sys_nachricht = json_message["sender_name"] + ":" + message
            print(sys_nachricht)
        elif json_message["nachrichten_id"] == 2:
            if json_message["aktion"] == "login":
                time_conv((json_message["zeitstempel"]))
                loggin = json_message["sender_name"] + " " + "just logged in"
                print(loggin)
            elif json_message["aktion"] == "logout":
                time_conv((json_message["zeitstempel"]))
                loggout = json_message["sender_name"] + " " + "just logged out"
                print(loggout)
    return

def main():
    global new_socket, username, mutex, serveradr
    begr_text()
    new_socket = connect()
    username = input("Geben sie einen Benutzernamen ein: ")
    # Hauptthreads werden gestartet
    thread1 = threading.Thread(target=send)
    thread1.start()
    thread2 = threading.Thread(target=get_message, args=(serveradr,))
    thread2.start()
                           
main()
