############################################################
# This python script is a producer for kafka.

# To send it to kafka, each record is first converted to
# string then to bytes using str.encode('utf-8') method.
#
# The parameters
# config.KAFKA_SERVERS: public DNS and port of the servers
# were written in a separate "config.py".
############################################################


import sys
import json
import yaml
import os
import time
import datetime
import random
from kafka import KafkaProducer

def main():

    producer = KafkaProducer(bootstrap_servers = 'ec2-34-221-97-108.us-west-2.compute.amazonaws.com:9092,ec2-54-186-45-58.us-west-2.compute.amazonaws.com:9092,ec2-54-190-0-79.us-west-2.compute.amazonaws.com:9092')

    f = open('1000_data.json', 'r')
    while True:
        msg = f.readline()
        if not msg:
            break
        producer.send('amtrans', msg.encode('utf-8'))
        producer.flush()
        print (msg)
        time.sleep(1)
    f.close()


    return

if __name__ == '__main__':
	main()
