import simple_socket, reverse, encrypt, threading
mutex = threading.Lock()

def sever_address():
    """returns the server address fro a user input
    or returns the standart address
    """
    print("Geben Sie die Serveradresse ein, oder tippen sie 's' für Standartadresse")
    serveradr = input()
    if serveradr == "s" or "S":
        serveradr = "127.0.0.1"
    return serveradr

def socket_starter(serveradr):
    """starts a server with simple sockets
    """
    print("Wollen sie sich als (S)erver oder (C)lient verbinden?")
    secli = input()
    if secli == "S" or "s":
        new_socket = simple_socket.connect_as_server(serveraddress=serveradr)
    elif secli == "C"  or "c":
        new_socket = simple_socket.connect_as_client(serveraddress=serveradr)
    return new_socket

def send_message(new_socket):
    """sends a message
    """
    global mutex
    mutex.acquire()
    message = input("Lukas: ")
    message = reverse.reverse(message)
    message = encrypt.encrypt_normal(message)
    new_socket.send(message)
    mutex.release()
    return

def receive_message(new_socket):
    """recieves a message
    """
    global mutex
    mutex.acquire()
    ben = new_socket.receive()
    ben = reverse.reverse(ben)
    ben = encrypt.decrypt_normal(ben)
    print("User 2:", ben)
    mutex.release()
    return


server_address()
socket_starter(serveradr)
new_socket.start()
thread1 = threading.Thread(target=send_message, args=(new_socket)
