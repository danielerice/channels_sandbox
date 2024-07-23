from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

import json

channel_layer = get_channel_layer()

class OrderConsumer(WebsocketConsumer):
    def connect(self):
        print('connect event')
        async_to_sync(self.channel_layer.group_add)("orders", self.channel_name)
        self.accept()

    def receive(self, event, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))

        print('receive event : ', event)


    def disconnect(self, close_code):
        print('close_code : ', close_code)
        async_to_sync(self.channel_layer.group_discard)("orders", self.channel_name)
        self.close()

    def new_order(self, event):
        print('new order :', event, type(event))
        print(event["content"].name, event['content'].description)
        self.send(json.dumps({
            'type':'new.order',
            'content': {
                'name' : event["content"].name,
                'desc' : event['content'].description
            }
        }))
        print('sent')

