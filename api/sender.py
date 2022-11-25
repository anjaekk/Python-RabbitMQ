import logging
import pika
from fastapi import FastAPI
from rabbitmq import Rabbitmq


app = FastAPI()


@app.get("/")
def root():
    queue = Rabbitmq(
        queue='test', 
        routing_key='test', 
        exchange='test_exchange'
    )
    queue.publish("Hello World")
    logging.info(" [x] Sent 'Hello World!' ")
    return {"connect":"success"}
