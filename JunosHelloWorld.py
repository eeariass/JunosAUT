#! /usr/bin/python3
#A "HelloWorld" PyEZ script

from jnpr.junos import Device

dev = Device(host="192.168.0.10", user="root", password="lab123")
dev.open()
print(dev.facts)
dev.close()
