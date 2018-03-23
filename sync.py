# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 12:32:53 2018

@author: cvssa
"""

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

import logging
import time
import argparse
import json
import ssl

cert_path = "c:/certs/"
host = "a2kc9la4cp40qj.iot.us-east-1.amazonaws.com"
returntopic = "$aws/things/ir2_proj/shadow/return"
sendtopic = "$aws/things/ir2_proj/shadow/update"
logtopic = "$aws/things/ir2_proj/log"
root_cert = cert_path + "root-CA.crt"
cert_file = cert_path + "ir2_proj.cert.pem"
key_file = cert_path + "ir2_proj.private.key"

logger = logging.getLogger('Robot')

# Intializes and sets Logging for the service
def logger_init():
    logger.setLevel(logging.DEBUG)
    log_file_size = 1024 * 1024 * 1  # 1 MB
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(process)d - %(name)s : %(message)s')
    fh = logging.handlers.RotatingFileHandler('/home/pi/logs/iot_robot.log', maxBytes=log_file_size, backupCount=5)
    fh.setFormatter(formatter)
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(sh)
    logger.info('******************************************')
    logger.info('.......Starting up proj Service........')
    
def on_message(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")

def on_connect(client, userdata, flags, rc):
    logger.info("connected with result code " + str(rc))
    robot.subscribe(sendtopic)
    robot.subscribe(returntopic)

# Initializing Logger      
#logger_init()
#logger.info('setting up mqtt client')

#starting service
robot = mqtt.Client(client_id="Send_msg.py")
logger.info('completed setting up mqtt client')
robot.on_connect = on_connect
robot.on_message = on_message
#client.on_log = on_log
robot.tls_set(root_cert,
               certfile = cert_file,
               keyfile = key_file,
               tls_version=ssl.PROTOCOL_TLSv1_2,
               ciphers=None)

robot.connect(host, 8883, 60)

robot.loop()
time.sleep(1)
time.sleep(1)

#robot.loop()
time.sleep(1)

robot.publish(sendtopic, '{ \"desired\":{ \"message\":\"off\"}}',1)

time.sleep(1)

#robot.disconnect()

#loops for ever so that connection will be present
while True:
	robot.loop()
	time.sleep(1)
