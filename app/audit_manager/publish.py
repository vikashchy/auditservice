import pika


# Create a new instance of the Connection object
def send_message(message=None):
    conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    print(conn.__str__())
    channel = conn.channel()
    channel.queue_declare(queue='audit_message')
    if message is not None:
        channel.basic_publish(exchange='', routing_key='audit_message', body=message)
        print(f"[x] Sent {message}")
    conn.close()




