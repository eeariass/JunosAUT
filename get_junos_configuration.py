#! /usr/local/bin/python3

import xmltodict
import sys
from pprint import pprint
from getpass import getpass
from jnpr.junos import *
from lxml import etree
import json

hostname = input('insert hostname or ip address: ')
username = input ('insert username: ')
passwd = getpass('insert password: ')

print('')

print('*** Device general information: ***')

with Device(host=hostname, user=username, password=passwd) as dev:
    configuration = dev.rpc.get_config(filter_xml=etree.XML('<configuration><interfaces/></configuration>'))
    toJson = json.dumps(xmltodict.parse((etree.tostring(configuration))))
    pprint(toJson)
