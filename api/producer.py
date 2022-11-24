import logging
import pika
from fastapi import FastAPI
from utils import ROUTING_KEY, RABBITMQ_QUEUE, parameters


app = FastAPI()


@app.get("/")
def root():
    try: 
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()  
        channel.queue_declare(queue=RABBITMQ_QUEUE)
        channel.basic_publish(exchange='', routing_key=ROUTING_KEY, body='Hello World!')
        logging.info(" [x] Sent 'Hello World!' ")
    finally:
        connection.close()
    return {"connect":"success"}
