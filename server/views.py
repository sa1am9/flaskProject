from flask import request, g, jsonify, abort, make_response, Blueprint
import json
import pika
import os
bp_task = Blueprint('bp_task', __name__, url_prefix='/task')

@bp_task.route('', methods=['POST'])
def task_add():
    create_task_mq(json.dumps(request.json))
    return  {'status': 'task send'}


def create_task_mq(text):
    credentials = pika.PlainCredentials(os.environ.get('RABBIT_USER'), os.environ.get('RABBIT_PASSWORD'))
    parameters = pika.ConnectionParameters(str(os.environ.get('RABBIT_HOST')),
                                           int(os.environ.get('RABBIT_PORT')),
                                           os.environ.get('RABBIT_VHOST'),
                                           credentials,
                                           heartbeat=30)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue=os.environ.get('RABBIT_QUEUE'))
    try:
        channel.basic_publish(exchange='',
                              routing_key=os.environ.get('RABBIT_QUEUE'),
                              body=str(text))
    except Exception as e:
        print('[ERROR] SEND TO MQ = ', e)
    connection.close()