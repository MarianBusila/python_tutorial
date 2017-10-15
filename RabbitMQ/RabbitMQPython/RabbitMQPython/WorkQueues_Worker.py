import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.queue_declare(queue = "task_queue", durable = True)

def callback(ch, method, properties, body):
    print (" [x] Received %r" %body)
    time.sleep(body.count(b'.'))
    print (" [x] Done")

    ch.basic_ack(delivery_tag = method.delivery_tag)

#don't dispatch a new message to a worker until it has processed and acknowledged the previous one
channel.basic_qos(prefetch_count = 1) 
channel.basic_consume(callback,
                      queue = "task_queue"
                      )

print (" [*] Waiting for tasks. Press CTRL + C to exit.")
channel.start_consuming()