from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'inference_logs',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def stream_logs():
    for msg in consumer:
        yield msg.value
