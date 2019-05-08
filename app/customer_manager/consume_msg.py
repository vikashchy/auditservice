import pika

message = ""


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    global message
    message = body


def get_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='audit_message')
    channel.basic_consume(queue='audit_message', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    channel.stop_consuming()
    # channel.


if __name__ == '__main__':
    get_messages()
    print(message)
