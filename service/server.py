import asyncio
import traceback

def handle_cmd(cmd):
    return 'not implement'

async def handle_connection(reader, writer):
    data = await reader.read(100) # ждем получение данных
    cmd_str = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {cmd_str!r} from {addr!r}")
    
    try:
        responce_cmd = handle_cmd(cmd_str)
    except Exception as e:
        responce_cmd = 'err: {0}'.format(e)
        print(traceback.format_exc())
    
    print(f"Send: {responce_cmd!r}")
    writer.write(responce_cmd.encode())
    await writer.drain() # ждем пока не придет время возобновить запись в поток

    print("Close the connection")
    writer.close()

async def server_async():
    server = await asyncio.start_server(
        handle_connection, '127.0.0.1', 49) # создаем и ждем создание сервера

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
    
    async with server:
        await server.serve_forever() # Начинает принимать соединения до тех пор, пока не будет отменена корутина.