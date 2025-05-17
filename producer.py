from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'localhost:9092'})

def delivery_report(err, msg):
    if err is not None:
        print('Error:', err)
    else:
        print(f'Mensaje entregado a {msg.topic()} [{msg.partition()}]')

p.produce('test', key='key', value='Hola mundo Kafka!', callback=delivery_report)
p.flush()
