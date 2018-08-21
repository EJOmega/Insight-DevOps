from __future__ import print_function

import sys
import json
import yaml
import os
import time
import datetime
import random
from kafka import KafkaConsumer

KAFKA_TOPIC = 'pmtrans'
KAFKA_BROKERS = 'ec2-34-221-97-108.us-west-2.compute.amazonaws.com:9092,ec2-54-186-45-58.us-west-2.compute.amazonaws.com:9092,ec2-54-190-0-79.us-west-2.compute.amazonaws.com:9092'



consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_BROKERS,
                         auto_offset_reset='earliest')



try:
    for message in consumer:
        print(message.value.decode('utf-8'))
except KeyboardInterrupt:
    sys.exit()
