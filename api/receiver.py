import logging
import pika

from rabbitmq import Rabbitmq

logging.basicConfig(level = logging.INFO)

def callback(channel, method, properties, body) -> None:
    logging.info(
        f' [x] Received {body.decode()} from queue'
    )

queue = Rabbitmq(
    queue='test', 
    routing_key='test', 
    exchange='test_exchange'
)
queue.consume(callback)
logging.info(
    " [*] Waiting for messages. To exit press CTRL+C "
)