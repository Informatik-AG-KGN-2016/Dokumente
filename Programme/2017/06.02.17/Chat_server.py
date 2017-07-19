import simple_socket, reverse, encrypt, threading

print("Geben Sie die Serveradresse ein, oder tippen sie 's' für Standartadresse")
serveradr = input()
if serveradr == "s" or "S":
    serveradr = "127.0.0.1"

new_socket = simple_socket.connect_as_server()

while True:
    message = input("Lukas: ")
    message = reverse. reverse(message)
    message = encrypt.encrypt_normal(message)
    new_socket.send(message)
    ben = new_socket.receive()
    ben = reverse.reverse(ben)
    ben = encrypt.decrypt_normal(ben)
    print("Ben:", ben)
    if message == "*close*":
        new_socket.close
