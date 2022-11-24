import os
import pika

RABBITMQ_HOST = os.environ['RABBITMQ_HOST']
RABBITMQ_QUEUE = os.environ['RABBITMQ_QUEUE']
ROUTING_KEY = os.environ['ROUTING_KEY']
RABBITMQ_USERNAME = os.environ['RABBITMQ_USERNAME']
RABBITMQ_PASSSWORD = os.environ['RABBITMQ_PASSSWORD']


credentials = pika.PlainCredentials(username=RABBITMQ_USERNAME, password=RABBITMQ_PASSSWORD)
parameters = pika.ConnectionParameters(RABBITMQ_HOST, credentials=credentials)
