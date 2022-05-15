import pika
import time

def create_connection():
    credentials = pika.PlainCredentials(username='user', password='pass')
    return pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672, credentials=credentials))

class Publisher:
    def __init__(self, config):
        self.config = config

    def publish(self, channel, message):
        channel.basic_publish(exchange=self.config['exchange'], routing_key=self.config['routing_key'], body=message)

if __name__=="__main__":
    time.sleep(20)
    connection = create_connection()
    channel = connection.channel()
    exchange, routing_key = 'my_exchange', "routing_key"
    channel.exchange_declare(exchange=exchange)
    channel.queue_declare(queue=exchange)
    channel.queue_bind(queue=exchange, exchange=exchange, routing_key=routing_key)
    publisher = Publisher({'exchange': exchange, "routing_key": routing_key})
    for x in range(1, 10000000):
        publisher.publish(channel, str({'name': 'message{0}'.format(str(x))}))

