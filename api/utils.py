import os
import pika

RABBITMQ_HOST = os.environ['RABBITMQ_HOST']
RABBITMQ_USERNAME = os.environ['RABBITMQ_DEFAULT_USER']
RABBITMQ_PASSSWORD = os.environ['RABBITMQ_DEFAULT_PASS']