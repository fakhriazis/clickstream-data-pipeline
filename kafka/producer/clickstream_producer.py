# kafka/producer/clickstream_producer.py

import json
import time
import random
from faker import Faker
from kafka import KafkaProducer

fake = Faker()

EVENT_TYPES = ['page_view', 'click', 'scroll', 'add_to_cart', 'checkout']

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_event():
    return {
        'user_id': fake.uuid4(),
        'event_type': random.choice(EVENT_TYPES),
        'url': fake.url(),
        'timestamp': fake.iso8601()
    }

if __name__ == "__main__":
    topic = 'clickstream_events'
    print(f"Producing to topic: {topic}")
    while True:
        event = generate_event()
        producer.send(topic, event)
        print(f"Produced: {event}")
        time.sleep(1)
