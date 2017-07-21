# Chat-Protokoll


import rotation_encryption, time, json

#packet = Packet()
#packet.nachrichten_id = 2
#packet.sender_name = "test"
#packet.aktion = "login"
#string = packet.to_json_string()
#
#packet2 = Packet(string)
#if packet2.nachrichten_id == 1:
#    print(packet2.sender_name + ": " + packet2.text)
#elif packet2.nachrichten_id == 2:
#    if packet2.aktion == "login":
#        print(packet2.sender_name + " hat sich eingeloggt!")
#    elif packet2.aktion == "logout":
#        print(packet2.sender_name + " hat sich ausgeloggt!")
#    elif packet2.aktion == "login_success":
#        print("Online Nutzer: " + str(packet2.bekannte_sender))



class Packet:

    def __init__(self, json_string=""):
        if json_string == "":
            return
        dictionary = json.loads(json_string)
        if "nachrichten_id" in dictionary:
            self.nachrichten_id = dictionary["nachrichten_id"]
            if self.nachrichten_id == 1:
                encryption_key = dictionary["verschlüsselung"]["parameter"][0]
                if "text" in dictionary["verschlüsselung"]["verschlüsselte_parameter"]:
                    self.text = rotation_encryption.decrypt(dictionary["text"], encryption_key)
                else:
                    self.text = dictionary["text"]
                if "sender_name" in dictionary["verschlüsselung"]["verschlüsselte_parameter"]:
                    self.sender_name = rotation_encryption.decrypt(dictionary["sender_name"], encryption_key)
                else:
                    self.sender_name = dictionary["sender_name"]
            elif self.nachrichten_id == 2:
                self.aktion = dictionary["aktion"]
                self.sender_name = dictionary["sender_name"]
                if self.aktion == "login_success":
                    self.bekannte_sender = dictionary["bekannte_sender"]
                
        
    def to_json_string(self):
        if self.nachrichten_id == 1:
            dictionary = {
                "nachrichten_id": self.nachrichten_id,
                "text": rotation_encryption.encrypt(self.text, self.encryption_key),
                "text_länge": len(self.text),
                "verschlüsselung":
                {
                    "algorithmus": "caesar",
                    "parameter": [self.encryption_key],
                    "verschlüsselte_parameter": ["text", "sender_name"]
                },
                "sender_name": rotation_encryption.encrypt(self.sender_name, self.encryption_key),
                "zeitstempel": time.time(),
                "protokoll_version": "0.2"
            }
            return json.dumps(dictionary)
        if self.nachrichten_id == 2:
            dictionary = {
                "nachrichten_id": self.nachrichten_id,
                "aktion": self.aktion,
                "sender_name": self.sender_name,
                "zeitstempel": time.time(),
                "protokoll_version": "0.2"
            }
            if self.aktion == "login_success":
                dictionary["bekannte_sender"] = self.bekannte_sender
            return json.dumps(dictionary)
