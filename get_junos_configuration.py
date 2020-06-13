#! /usr/local/bin/python3

import sys
from pprint import pprint
from getpass import getpass
from jnpr.junos import Device
from lxml import etree

hostname = input('insert hostname or ip address: ')
username = input ('insert username: ')
passwd = getpass('insert password: ')

print('')

print('*** Device general information: ***')

with Device(host=hostname, user=username, password=passwd) as dev:
    config = dev.rpc.get_config(filter_xml=etree.XML('<configuration></configuration>'))
    print(etree.tostring(config))
