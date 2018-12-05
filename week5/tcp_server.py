# asyncio, tcp сервер

import asyncio

async def handle_echo(reader, writer):
    data = await reader.read(1024)
    message = data.decode()
    addr = writer.get_extra_info("peername")
    print("received %r from %r" % (message, addr))
    writer.close()

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, "127.0.0.1", 8081, loop=loop)
server = loop.run_until_complete(coro)

async def wakeup():
    while True:
        await asyncio.sleep(1)
# add wakeup HACK
loop.create_task(wakeup())

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
