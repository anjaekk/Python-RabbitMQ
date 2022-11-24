import logging
import pika

from utils import RABBITMQ_QUEUE, parameters

logging.basicConfig(level = logging.INFO)

def callback(channel, method, properties, body):
    logging.info(f' [x] Received {body.decode()} from queue')

connection = pika.BlockingConnection(parameters)
channel = connection.channel()  
channel.queue_declare(queue=RABBITMQ_QUEUE)
channel.basic_consume(queue=RABBITMQ_QUEUE, auto_ack=True, on_message_callback=callback)

logging.info(" [*] Waiting for messages. To exit press CTRL+C ")
channel.start_consuming()