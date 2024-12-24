import nsq
import tornado.ioloop

def message_handler(message):
    print(f"Received message: {message.body.decode()}")
    return True  # Acknowledge the message

# Connect directly to nsqd instead of lookupd
reader = nsq.Reader(
    message_handler=message_handler,
    topic='test',
    channel='ephemeral_channel#ephemeral',
    nsqd_tcp_addresses=['127.0.0.1:4150']  # Directly connect to nsqd
)

tornado.ioloop.IOLoop.current().start()

