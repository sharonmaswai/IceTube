from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import Message

class ChatConsumer(WebsocketConsumer):
    def fetch_messages(self, data):
        messages= Message.last_12_messages()
        content={
            'messages': self.messages_to_json(messages)
        }
        self.send_chat_message(content)
    def new_message():
        print('new message')
        pass

        self.accept()
    def messages_to_json(self, messages ):    
        result=[]
        for message in messages: 
            result.append(self.messages_to_json(messages))
        return result
    def message_to_json(self, message ) :  
        return{
            'author':message.author.username
            'content':message.content,
            'timesent':str(message.timesent)  
             
    
    }  
    
    commands = {
        'fetch_messages': fetch_messages
        'new_message':new_message
    } 
    
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
    
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )   
    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
    def send_chat_message(self, message):
        
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))