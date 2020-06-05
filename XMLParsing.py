#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 18:26:26 2020

@author: elvarias
"""

#Perform the necessary imports
from jnpr.junos import Device
from lxml.etree import dump, _Element
from sys import argv

#Use 1st command-line parameter as XPATH, or use "." if it is not provided.
conf_xpath = argv[1] if len(argv) > 1 else "."

#Username, password and device IP
USER = "root"
PASSWD = "lab123"
DEVICE_IP = "192.168.0.10"

#Open NETCONF connection using PyEZ Device class
with Device(host=DEVICE_IP, user=USER, password=PASSWD) as dev:
    #Read a complete config using <get-config> RPC
    full_config = dev.rpc.get_config()
    #Filter the config with provided XPATH
    filtered_config = full_config.xpath(conf_xpath)
    #The result of applying XPATH is a list - perform for each loop
    for entry in filtered_config:
        #For each entry, print it either using dump() or print() functions
        if type(entry) is _Element:
            dump(entry)
        else:
            print(entry)
