
# This service is meant to publish extracted data to those who would listen..
# With RabbitMQ implementation, using a single queue means that data would be heard by one listener at a time..

import json
import pika,os

from pika.exchange_type import ExchangeType

RMQ_HOST = str(os.getenv("RABBIT_MQ_HOST"))
print(RMQ_HOST)
RMQ_PORT = str(os.getenv("RABBIT_MQ_PORT"))
print(RMQ_PORT)
RMQ_USER = str(os.getenv("RABBIT_MQ_USER"))
print(RMQ_USER)
RMQ_PASSWORD = str(os.getenv("RABBIT_MQ_PASSWORD"))
print(RMQ_PASSWORD)
EXCHANGE = str(os.getenv("RABBIT_MQ_EXCHANGE"))
print(EXCHANGE)

creds = pika.PlainCredentials(username=RMQ_USER,password=RMQ_PASSWORD)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RMQ_HOST,credentials=creds))
channel = connection.channel()

channel.queue_declare(queue='Twitter')
channel.exchange_declare(EXCHANGE,exchange_type=ExchangeType.direct)
# channel.queue_bind(exchange=EXCHANGE, queue='Twitter')

with open('graphe') as f:
    dateien = json.load(f)


# dateien["roadmap"]= []

# print(dateien["nodes"])

# channel.basic_publish(exchange="storage", routing_key="Twitter", body=json.dumps({"h":[]}))
channel.basic_publish(exchange=EXCHANGE, routing_key='Youtube', body=json.dumps(dateien))
# channel.basic_publish(exchange=EXCHANGE, routing_key='Twitter', body=json.dumps({"h":[1,2],"roadmap":[]}))
# channel.basic_publish(exchange=EXCHANGE, routing_key='Twitter', body=json.dumps({"h":[1,2],"roadmap":[]}))
# channel.basic_publish(exchange=EXCHANGE, routing_key='Twitter', body=json.dumps({"h":[1,2],"roadmap":[]}))
# channel.basic_publish(exchange=EXCHANGE, routing_key='Twitter', body=json.dumps({"h":[1,2],"roadmap":[]}))
print(" [x] Sent linked data!")
connection.close()

# class publisherImplementation:
    
#     def __init__(self,exchange,user=RMQ_USER,password=RMQ_PASSWORD,*args):   
        
#         self.credentials = pika.PlainCredentials(user,password)
#         self.connection= pika.BlockingConnection(pika.ConnectionParameters(host=RMQ_HOST,credentials=self.credentials))#, credentials= self.credentials
#         self.channel= self.connection.channel()
#         self.channel.exchange_declare(exchange=exchange, exchange_type=ExchangeType.direct)
#         # self.addQueue("Context","token")

    
#     def addQueue(self,routeName,queueName):
#         self.channel.queue_declare(queue= queueName)
#         self.channel.queue_bind(exchange=EXCHANGE, queue=queueName, routing_key=routeName)
    
#     def updateVariable(self):
#         pass
    
    
#     def publish(self,routeName,data):
#         print("Eureka!!, es geht!")
#         self.channel.basic_publish(exchange=EXCHANGE,routing_key = routeName ,body = data)
