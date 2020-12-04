import pika
import os
def get_connection():
  MQ_USER = os.environ.get('RABBIT_USER')
  MQ_PASS = os.environ.get('RABBIT_PASSWORD')
  MQ_SERVER = os.environ.get('RABBIT_HOST')
  MQ_VHOST = os.environ.get('RABBIT_VHOST')
  MQ_PORT = int(os.environ.get('RABBIT_PORT'))
  credentials = pika.PlainCredentials(MQ_USER, MQ_PASS)

  connection = pika.BlockingConnection(pika.ConnectionParameters(MQ_SERVER, MQ_PORT, MQ_VHOST, credentials))
  return connection