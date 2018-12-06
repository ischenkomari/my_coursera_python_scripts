"""TCP client"""
import socket
import time


class Client:
    """Client class"""
    def __init__(self, host, port, timeout=None):
        self.host = str(host)
        self.port = int(port)
        self.timeout = timeout

    def connection(self, message):
        """Server connection"""
        with socket.create_connection((self.host, self.port)) as sock:
            sock.settimeout(self.timeout)
            sock.sendall(str(message).encode())
            server_responce = sock.recv(1024).decode("utf8")
            print(server_responce)
        return server_responce

    def get(self, message):
        """get responce from server"""
        message = "get {}".format(message)
        server_responce = dict()
        server_responce = self.connection(message)
        return server_responce

    def put(self, metric_name, value, timestamp=None):
        """pull some metric to the server"""
        if timestamp is None:
            timestamp = str(int(time.time()))
        message = "put {} {} {}".format(metric_name, timestamp, value)
        try:
            self.connection(message)
        except Exception as er:
            print(er)

def _main():
    client = Client("127.0.0.1", 8181, timeout=15)

    client.put("palm.cpu", 0.5, timestamp=1150864247)
    client.put("palm.cpu", 2.0, timestamp=1150864248)
    client.put("palm.cpu", 0.5, timestamp=1150864248)

    client.put("eardrum.cpu", 3, timestamp=1150864250)
    client.put("eardrum.cpu", 4, timestamp=1150864251)
    client.put("eardrum.memory", 4200000)

    client.get("palm.cpu")
    client.get("*")
    client.get("non_existing_key")


if __name__ == "__main__":
    _main()
