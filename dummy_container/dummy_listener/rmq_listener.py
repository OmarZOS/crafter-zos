
import json
import os

import pika
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





class rabbitMQ_Implementation:
    
    def __init__(self,exchange,hostName=RMQ_HOST,user=RMQ_USER,password=RMQ_PASSWORD):#,routeName,user,password,portNumber,hostName="localhost",exchange="data"
        
        # keeping the shared variable
        # self.available_services = services
        
        creds = pika.PlainCredentials(username=user,password=password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostName,credentials=creds,port=RMQ_PORT))#port=portNumber, ,  credentials= self.credentials
        channel = connection.channel()
        print (exchange)
        api = "Twitter"
        channel.exchange_declare(exchange,exchange_type=ExchangeType.direct)#durable=True,
        
        # for api in QUEUES: # each queue is dynamically declared
        channel.queue_declare(queue=api)
        channel.queue_bind(queue=api,exchange=exchange,routing_key=api)
        # for api in QUEUES: # each queue is dynamically started
        channel.basic_consume(queue=api, on_message_callback=self.universal_receiver(api), auto_ack=True)
        
        channel.start_consuming()
        
        
        
    def universal_receiver(self,api_name): # it could be done in a simpler way.. It's just something that I alaways wanted to try..
        return lambda ch, method, properties, body : self.receiveData(api_name,ch, method, properties, body) # das ist kûnst..
    
    def receiveData(self,api_name,ch,method,properties,body):
        print("")
        print("")
        print(body.decode())
        # try:
        print(json.loads(body.decode()))
        # self.handle_data(api_name,json.loads(body.decode()))
        # except :
        #     print(0)
        #     pass
    # def handle_data(args):
    #     pass
        
        
if __name__=="__main__":
    listener = rabbitMQ_Implementation(EXCHANGE)