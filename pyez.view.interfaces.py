#!/usr/local/bin/python3

from jnpr.junos import Device
from pprint import pprint
from lxml import etree
from getpass import getpass
import sys

#jhost=input('Enter hostname / host ip: ')
#juser=input('Enter username: ')
#jpass=getpass('Enter password: ')

jhost='192.168.0.10'
juser='root'
jpass='lab123'

dev=Device(host=jhost, user=juser, password=jpass)
dev.open()
jinterfaces = dev.rpc.get_config('interfaces', options={'format':'json'})

print('\n')
print('The interface information is: \n')
print(jinterfaces, '\n')

print('The interfaces present in this configuration are: ')
for interfaces in jinterfaces['configuration']['interfaces']['interface'][0]['unit']:
    print(interfaces['family'][0])
    #print(interfaces['filter'])



#print('\n')
#print('*** ### The general information of the device is ### ***\n')
#pprint(dev.facts)

dev.close()
