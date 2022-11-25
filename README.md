# Python-RabbitMQ

## Stack
- Fastapi
- RabbitMQ
- docker-compose

## How to use
Docker and docker-compose must be installed to follow the next step. 
Create images and run the contatiners.  

- API container
- RabbitMQ container

```
docker-compose up -d 
```

## Project Structure
```
├── api
│   ├── Dockerfile
│   ├── producer.py
│   ├── receiver.py
│   ├── requirements.txt
│   └── utils.py
└── docker-compose.yml

```

## Environment Variables
```
RABBITMQ_DEFAULT_USER
RABBITMQ_DEFAULT_PASS
RABBITMQ_USERNAME
RABBITMQ_PASSSWORD
RABBITMQ_HOST
RABBITMQ_QUEUE
ROUTING_KEY
```
