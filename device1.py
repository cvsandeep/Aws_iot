from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import argparse
import json

cert_path = "/home/pi/certs/"
host = "a2kc9la4cp40qj.iot.us-east-1.amazonaws.com"
returntopic = "$aws/things/ir2_proj/shadow/return"
sendtopic = "$aws/things/ir2_proj/shadow/send"
root_cert = "/home/pi/certs/root-CA.crt"
cert_file = cert_path + "ir2_proj.cert.pem"
key_file = cert_path + "ir2_proj.private.key"


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
    

# Initializing Logger      
logger_init()
logger.info('setting up mqtt client')

#starting service
robot = AWSIoTMQTTClient(clientId)
robot.configureEndpoint(host, 8883)
robot.configureCredentials(root_cert, key_file, cert_file)
logger.info('completed setting up mqtt client')

# AWSIoTMQTTClient connection configuration
robot.configureAutoReconnectBackoffTime(1, 32, 20)
robot.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
robot.configureDrainingFrequency(2)  # Draining: 2 Hz
robot.configureConnectDisconnectTimeout(10)  # 10 sec
robot.configureMQTTOperationTimeout(5)  # 5 sec
logger.info('completed setting up mqtt client')

# Connect and subscribe to AWS IoT
myAWSIoTMQTTClient.connect()

robot.loop()
time.sleep(1)
robot.publish(sendtopic, 'MyHomeService started')

#loops for ever so that connection will be present
while True:
	robot.loop()
	time.sleep(1)
