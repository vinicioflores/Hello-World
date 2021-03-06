#### Module to enqueue & dequeue messages into our Messaging Middleware of choice (async) communication - in this case RabbitMQ which is AMQP standard compliant
#### HTTP gateway is the one who'll leverage this the most

import pika, os
import uuid

class Bus:

	busUrl = 'amqp://guest:guest@localhost/%2f'  
	busParams = pika.URLParameters(busUrl)
	busParams.socket_timeout=10
	busConnection = 'nil'
	busQueues =  {"dummy_queue", "nil"}


	def __init__ (self, url, timeout):
		self.busParams = pika.URLParameters(url)
		self.busParams.socket_timeout=timeout
		StartBusProtocol()
		
	def AddQueue(self, name):
		self.busQueues[name] = connection.channel()
		self.busQueues[name].queue_declare(queue=name)
		
	def EnqueueMessage(self, queueName, message):
		self.busQueues[queueName].basic_publish(exchange='', routing_key=queueName, body=message)
		
	def SubscribeQueue(self, queueName, callback):
		self.busQueues[queueName].basic_consume(queueName, callback, auto_ack=True)
		
	def StreamQueue(self, queueName):
		self.busQueues[queueName].start_consuming()
		return self.busQueues[queueName]
	
	def StartBusProtocol(self):
		self.busConnection=pika.BlockingConnection(self.busParams) # connect to RabbitMQ
		AddQueue(self, 'product')
		AddQueue(self, 'inventory')
		AddQueue(self, 'suppliers')
		
	def StopBusProtocol(self):
		self.busConnection.close()
		




