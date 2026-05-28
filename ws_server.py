from fastapi import WebSocket

connections = []

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connections.append(websocket)

    while True:
        data = await websocket.receive_text()

        for conn in connections:
            await conn.send_text(data)
