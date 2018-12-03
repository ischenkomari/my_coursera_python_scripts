import socket

with socket.create_connection(("127.0.0.1, 10001"),5) as sock:
    sock.settimeout(2)
    try:
        sock.sendall("ping",encode("utf8"))
    except socket.error as er:
        print("send data error:", er) 
