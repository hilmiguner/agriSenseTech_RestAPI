from websocket_server import WebsocketServer

def new_client(client, server):
    print("New client connected!")
    server.send_message_to_all("Hey all, a new client has joined us")

def message_received(client, server, message):
    print(f"Received: {message}")
    server.send_message_to_all(message)

server = WebsocketServer(host="145.239.134.25", port=12345)
server.set_fn_new_client(new_client)
server.set_fn_message_received(message_received)
server.run_forever()