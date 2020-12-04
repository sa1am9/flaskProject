from worker.main_process import main_worker
import os
from dotenv import load_dotenv
from worker.Rabbit import ReconnectingConsumer

load_dotenv()
def main():
    amqp_url = 'amqp://{}:{}@{}:{}/{}'.format(os.environ.get('RABBIT_USER'), os.environ.get('RABBIT_PASSWORD'),
                       os.environ.get('RABBIT_HOST'), os.environ.get('RABBIT_PORT'),
                       os.environ.get('RABBIT_VHOST'))
    consumer = ReconnectingConsumer(amqp_url, main_worker)
    consumer.run()

main()
