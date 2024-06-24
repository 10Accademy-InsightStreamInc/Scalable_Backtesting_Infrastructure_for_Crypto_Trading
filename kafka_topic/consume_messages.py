from kafka_config import get_kafka_consumer, RESULT_TOPIC
from kafka import KafkaConsumer
import json

consumer = get_kafka_consumer(RESULT_TOPIC)

for message in consumer:
    backtest_result = message.value
    print(f"Received backtest result: {backtest_result}")
    # Process the backtest result as needed
