import pika
import json
import logging


class QueueService:

    def publish_wallet_creation(self,payload):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.76'))

            channel = connection.channel()

            channel.queue_declare(queue='wallet_creation', durable=True)

            message = json.dumps(payload)
            channel.basic_publish(
                exchange='',
                routing_key='wallet_creation',
                body=message,
                properties=pika.BasicProperties(
                    delivery_mode=2  
                )
            )
            logging.info(f"Wallet creation request published: {message}")
            connection.close()
        except Exception as e:
            logging.error(f"Failed to publish wallet creation: {e}")
