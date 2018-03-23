import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import logging, logging.handlers, traceback
import json, math, time, sys, ssl

cert_path = "/home/pi/certs/"
host = "a2kc9la4cp40qj.iot.us-east-1.amazonaws.com"
returntopic = "$aws/things/cvshome/shadow/return"
sendtopic = "$aws/things/cvshome/shadow/send"
root_cert = "/home/pi/certs/root-CA.crt"
cert_file = cert_path + "77c7086401-certificate.pem.crt"
key_file = cert_path + "77c7086401-private.pem.key"


robot= AWSIoTMQTTClient(clientId)

oyAWSIoTMQTTClient.configureEndpoint(host, 8883)
myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTClient connection configuration
  myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
            myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
            myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
            myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
            myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
