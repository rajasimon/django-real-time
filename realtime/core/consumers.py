from channels.generic.websocket import WebsocketConsumer


class RealTimeConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data="Return message from backend")

    def disconnect(self, code):
        print("Connection is disconnected")
