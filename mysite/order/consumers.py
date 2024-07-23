from channels.consumer import AsyncConsumer
import json

class OrderConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('connect event : ', event)
        await self.send({
            'type':'websocket.accept'
        })

    async def websocket_receive(self, event, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))

        print('receive event : ', event)

    async def websocket_disconnect(self, event):
        print('disconnect event : ', event)