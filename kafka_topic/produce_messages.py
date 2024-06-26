from kafka_config import get_kafka_producer, SCENE_TOPIC
import json

producer = get_kafka_producer()

def send_scene_parameters(scene_parameters):
    producer.send(SCENE_TOPIC, scene_parameters)
    producer.flush()
    print(f"Sent scene parameters: {scene_parameters}")

if __name__ == "__main__":
    scene_parameters = {
        'period': 20,
        'indicator_name': 'SMA',
        'start_date': '2021-01-01',
        'end_date': '2021-12-31'
    }
    send_scene_parameters(scene_parameters)
