import pika
from collections.abc import Callable

from utils import (
    RABBITMQ_USERNAME as username, 
    RABBITMQ_PASSSWORD as password, 
    RABBITMQ_HOST as host
)


class Rabbitmq:
    """ RabbitMQ definition class """
    def __init__(
        self, queue, routing_key=None, exchange='', exchange_type='direct'
        ) -> None:
        self._connection = None
        self._channel = None
        self._queue = queue
        self._username = username
        self._password = password
        self._host = host
        self._routing_key = routing_key
        self._exchange = exchange
        self._exchange_type = exchange_type
        self._rabbitmq()


    def _rabbitmq(self) -> None:
        self._create_channel()
        self._create_exchange()
        self._create_queue()
        self._create_bind()


    def _create_channel(self) -> None:
        credentials=pika.PlainCredentials(
            username=self._username, password=self._password
        )
        parameters = pika.ConnectionParameters(
            self._host, credentials=credentials
        )
        self._connection=pika.BlockingConnection(parameters)
        self._channel=self._connection.channel()


    def _create_exchange(self) -> None:
        self._channel.exchange_declare(
            exchange=self._exchange,
            exchange_type=self._exchange_type    
        )
    

    def _create_queue(self) -> None:
        self._channel.queue_declare(queue=self._queue)
    

    def _create_bind(self) -> None:
        self._channel.queue_bind(
            exchange=self._exchange, 
            queue=self._queue
        )


    def publish(self, body: str) -> None:
        self._channel.basic_publish(
            exchange=self._exchange,
            routing_key=self._routing_key,
            body=body
        )
    
    def consume(self, callback: Callable[[object], str]) -> None:
        self._channel.basic_consume(
            queue=self._queue,
            auto_ack=True,
            on_message_callback=callback
        )
        self._channel.start_consuming()