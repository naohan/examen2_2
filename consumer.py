from confluent_kafka import Consumer

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mi_grupo',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['test'])

print("Esperando mensajes (Ctrl+C para salir)...")
try:
    while True:
        msg = c.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Error:", msg.error())
        else:
            print(f'Mensaje recibido: {msg.value().decode("utf-8")}')
except KeyboardInterrupt:
    print("Detenido por el usuario.")
finally:
    c.close()
