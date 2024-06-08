import json
from websocket_server import WebsocketServer

# Bağlı istemcileri saklamak için bir sözlük
clients = {}

def new_client(client, server):
    print(f"New client connected: {client['address']}")
    clients[client['address'][0]] = client

def client_left(client, server):
    print(f"Client({client['address']}) disconnected")
    if client['address'][0] in clients:
        del clients[client['address'][0]]

def message_received(client, server, message):
    print(f"Received from client {client['address']}")
    try:
        data = json.loads(message)
        target_client = clients[data["target_ip"]]
        server.send_message(target_client, json.dumps(data["data"]))
        # if data['type'] == 'broadcast':
        #     server.send_message_to_all(data['message'])
        # elif data['type'] == 'private':
        #     target_id = data['target_id']
        #     if target_id in clients:
        #         server.send_message(clients[target_id], data['message'])
        #     else:
        #         server.send_message(client, "Target client not found.")
    except Exception as e:
        print(e)

server = WebsocketServer(host="0.0.0.0", port=12345)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
