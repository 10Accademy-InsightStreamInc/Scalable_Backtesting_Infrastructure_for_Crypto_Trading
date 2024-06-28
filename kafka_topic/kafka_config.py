from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import KafkaError
import json

KAFKA_BROKER_URL = 'g3.10academy.org:9092'
SCENE_TOPIC = 'scene_parameters'
RESULT_TOPIC = 'backtest_results'

def get_kafka_producer():
    return KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        max_request_size=209715200,  # 200 MB
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

def get_kafka_consumer(topic):
    return KafkaConsumer(
        topic,
        bootstrap_servers=KAFKA_BROKER_URL,
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        max_partition_fetch_bytes=209715200,
        group_id='my-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
