import json, simple_socket, sys, threading, time
from PyQt4.QtGui import *
from chat_protokoll import Packet

def clearLayout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()
        elif child.layout():
            clearLayout(child.layout())


class ChatProgram(QWidget):

    def __init__(self):
        
        super().__init__()
        v_box = QVBoxLayout()                           # erzeuge und setze vertikales Haupt-Layout
        self.setLayout(v_box)
        
        self.__running = False
        self.__nickname = None
        self.__my_socket = None
        self.__socket_input_thread = None
        self.__known_users = []

        self.show()                                     # mache Fenster sichtbar
        


    # Initialisiert das Launch-Fenster
    def init_launch_ui(self):
        clearLayout(self.layout())                      # leere das Fenster

        v_box = self.layout()

        self.resize(480, 240)
        
        self.setWindowTitle("Launch Chat")              # setze den Fenster-Titel

        self.label1 = QLabel("Server-Adresse: ")        # erzeuge Label und Eingabe-Feld für IP-Adresse
        self.line1 = QLineEdit()
        h_box = QHBoxLayout()
        h_box.addWidget(self.label1)
        h_box.addWidget(self.line1)
        v_box.addLayout(h_box)

        self.label2 = QLabel("Server-Port: ")           # erzeuge Label und Eingabe-Feld für Port
        self.line2 = QLineEdit()
        h_box = QHBoxLayout()
        h_box.addWidget(self.label2)
        h_box.addWidget(self.line2)
        v_box.addLayout(h_box)
        
        self.label3 = QLabel("Username: ")              # erzeuge Label und Eingabe-Feld für Username
        self.line3 = QLineEdit()
        h_box = QHBoxLayout()
        h_box.addWidget(self.label3)
        h_box.addWidget(self.line3)
        v_box.addLayout(h_box)

        self.button_login = QPushButton("Verbinden")    # erzeuge Button zum Verbinden
        self.button_login.clicked.connect(self.connect)
        v_box.addWidget(self.button_login)

        self.line1.returnPressed.connect(self.connect)  # Enter drücken zum Verbinden
        self.line2.returnPressed.connect(self.connect)
        self.line3.returnPressed.connect(self.connect)


    def connect(self):
        self.__server_address = self.line1.text()              # lese IP-Adresse und Port aus
        self.__server_port = self.line2.text()

        try:
            self.__server_port = int(str(self.__server_port))         # konvertiere Port zu Ganzzahl
        except:
            return

        self.__my_socket = simple_socket.connect_as_client(self.__server_address, self.__server_port)

        if not self.__my_socket:                        # prüfe ob Verbindung erfolgreich war
            return

        self.__nickname = self.line3.text()             # lese Username aus

        self.__my_socket.send(self.create_packet_2(self.__nickname, "login"))       # sende Login-Paket
        
        self.__socket_input_thread = threading.Thread(target=self.socket_input_runnable, args=())

        self.init_chat_ui()                             # starte Thread und neue Darstellung

        self.__running = True

        self.__socket_input_thread.start()


    def init_chat_ui(self):

        clearLayout(self.layout())                      # leere das Fenster

        self.resize(720, 480)
        
        self.setWindowTitle("Chat")                     # setze Fenster-Titel

        self.chat = QTextEdit()                         # erzeuge Nur-Lese-Textfeld für den Chat-Verlauf
        self.chat.setReadOnly(True)

        self.users = QTextEdit()                        # erzeuge Nur-Lese-Textfeld für die Senderliste
        self.users.setReadOnly(True)

        self.line = QLineEdit()                         # erzeuge Ein-Zeilen-Textfeld zum Schreiben
        self.line.returnPressed.connect(self.send_message)    # Enter drücken sendet Nachricht

        self.button = QPushButton("Senden")             # erzeuge "Senden"-Button
        self.button.clicked.connect(self.send_message)

        h1_box = QHBoxLayout()
        h1_box.addWidget(self.chat)
        h1_box.addWidget(self.users)

        h2_box = QHBoxLayout()                           # erzeuge horizontales Layout für Textfeld und Button
        h2_box.addWidget(self.line)
        h2_box.addWidget(self.button)

        v_box = self.layout()                           # füge alle Objekte zum vertikalen Haupt-Layout hinzu
        v_box.addLayout(h1_box)
        v_box.addLayout(h2_box)

    
    def create_packet_1(self, sender, message):
        packet = Packet()
        packet.nachrichten_id = 1
        packet.sender_name = str(sender)
        packet.text = str(message)
        packet.encryption_key = len(packet.text) % 26
        return packet.to_json_string()

    
    def create_packet_2(self, sender, action):
        packet = Packet()
        packet.nachrichten_id = 2
        packet.sender_name = str(sender)
        packet.aktion = str(action)
        return packet.to_json_string()


    def send_message(self):
        line = self.line.text()
        self.chat.append(self.__nickname + ": " + line)
        json_string = self.create_packet_1(self.__nickname, line)
        if not self.__my_socket.send(json_string):
            self.disconnect()
        self.line.setText("")
            

    def disconnect(self):
        self.__running = False
        if self.__my_socket:
            json_string = self.create_packet_2(self.__nickname, "logout")
            self.__my_socket.send(json_string)
        sys.exit()


    def socket_input_runnable(self):
        while self.__running:
            json_string = self.__my_socket.receive()
            if json_string:
                packet = Packet(json_string)
                if packet.nachrichten_id == 1:
                    self.chat.append(packet.sender_name + ": " + packet.text)
                elif packet.nachrichten_id == 2:
                    if packet.aktion == "login":
                        self.chat.append(packet.sender_name + " hat den Chatraum betreten!")
                        self.__known_users.append(packet.sender_name)
                    elif packet.aktion == "logout":
                        self.chat.append(packet.sender_name + " hat den Chatraum verlassen!")
                        self.__known_users.remove(packet.sender_name)
                    elif packet.aktion == "login_success":
                        self.__known_users = packet.bekannte_sender
                    self.users.clear()
                    for user in self.__known_users:
                        self.users.append(user)
            else:
                self.disconnect()
                


app = QApplication(sys.argv)
chat_program = ChatProgram()
app.aboutToQuit.connect(chat_program.disconnect)
chat_program.init_launch_ui()
sys.exit(app.exec_())
