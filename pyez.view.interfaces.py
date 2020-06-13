#!/usr/local/bin/python3

from jnpr.junos import Device
from pprint import pprint
from lxml import etree
from getpass import getpass
import sys

jhost=input('Enter hostname / host ip: ')
juser=input('Enter username: ')
jpass=getpass('Enter password: ')

dev=Device(host=jhost, user=juser, password=jpass)
dev.open()
print('*** ### The general information of the device is ### ***')
pprint(dev.facts)
dev.close()
