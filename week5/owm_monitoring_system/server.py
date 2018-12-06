"""TCP server of metrics"""
import asyncio
import json
import os.path


class ClientServerProtocol(asyncio.Protocol):
    """Class implamentation server protocol"""

    def connection_made(self, transport):
        self.transport = transport
        self.storage_path = "db.json"

    def process_data(self, data):
        """Processing recived data"""
        data = data.split()
        my_dict = dict()
        if data[0] == "put":
            my_dict = self.read_dict()
            content = [data[2], data[3]]
            if data[1] in my_dict:
                my_dict[data[1]].append(content)
            else:
                my_dict[data[1]] = [content]
            my_dict[data[1]].sort(key=lambda tup: tup[1])
            self.write_dict(my_dict)
            resp = "ok\n\n"
        elif data[0] == "get":
            my_resp = str()
            if data[1] == "*":
                my_dict = str(self.read_dict())
            else:
                try:
                    my_dict = self.read_dict()[data[1]]
                    my_dict = {data[1]: my_dict}
                except KeyError:
                    pass
            my_resp = str(my_dict)
            resp = "ok\n" + my_resp + "\n"
        else:
            resp = "error\nwrong command\n\n"
        return resp

    def data_received(self, data):
        print(data.decode())
        resp = self.process_data(data.decode())
        print(resp)
        self.transport.write(resp.encode())

    def read_dict(self):
        """Reading from storage"""
        if os.path.exists(self.storage_path):
            with open(self.storage_path) as file:
                my_dict = json.load(file)
        else:
            my_dict = dict()
        return my_dict

    def write_dict(self, my_dict):
        """Writing to storage"""
        with open(self.storage_path, 'w') as file:
            json.dump(my_dict, file)


def _main():
    async def wakeup():
        """ Dirty hack for Windows"""
        while True:
            await asyncio.sleep(1)


    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        '127.0.0.1', 8181
    )

    server = loop.run_until_complete(coro)

    # add wakeup  Dirty hack for Windows
    loop.create_task(wakeup())

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

if __name__ == "__main__":
    _main()
