import asyncio
import json


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def process_data(self, data):
        storage_path = "db.json"
        data = data.split()
        if data[0] == "put":
            my_dict = self.read_dict(storage_path)
            if data[1] in my_dict:
                my_dict[data[1]].append(tuple((data[3], data[2])))
            else:
                my_dict[data[1]] = [(data[3], data[2])]
            self.write_dict(storage_path, my_dict)
            resp = "ok\n\n"
        elif  data[0] == "get":
            my_resp = str()
            if data[1] == "*":
                my_resp = json.dumps(self.read_dict(storage_path)) + "\n"
            else:
                my_dict = json.dumps(self.read_dict(storage_path)[data[1]][0])
                if my_dict:
                    my_resp = "{" + data[1] + ": " + my_dict + "}"
            resp = "ok\n" + my_resp + "\n"
        else:
            resp = "error\nwrong command\n\n"
        return resp

    def data_received(self, data):
        print(data.decode())
        resp = self.process_data(data.decode())
        print(resp)
        self.transport.write(resp.encode())

    def read_dict(self, storage_path):
        try:
            with open(storage_path) as f:
                my_dict = json.load(f)
        except Exception as e:
            my_dict = dict()
        return my_dict

    def write_dict(self, storage_path, my_dict):
        with open(storage_path, 'w') as f:
            json.dump(my_dict, f)

# Dirty hack for Windows
async def wakeup():
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
