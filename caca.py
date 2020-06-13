#! /usr/local/bin/python3 
import pprint
from jnpr.junos import Device
import json

dev = Device(host='192.168.0.10', user='root', password='lab123')
dev.open()
print(dev.facts)
dev.close()
