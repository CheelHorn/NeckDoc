from fastapi import APIRouter, WebSocket, WebSocketDisconnect


router = APIRouter(
    prefix="/video_stream",
    tags=["video_stream"],
)

@router.websocket("/")
async def video_stream(websocket: WebSocket):
    await websocket.accept()
    x = 0
    try:
        while True:
            data = await websocket.receive_bytes()
            await websocket.send_json({"value": x,})
            x += 1
    except WebSocketDisconnect:
        print("Websocket connection disconnected by client")
    except Exception as e:
        print(e)
    finally:
        print("saving images")
        #pickle.dump(image_list, open("image_list.pkl", "wb"))
        if websocket.client_state == 1:
            await websocket.close()