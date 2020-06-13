#! /usr/local/bin/python3

from jnpr.junos import Device

dev = Device(host='192.168.0.10', user='root', password='lab123')
dev.open()
getOperationalBGP = dev.rpc.get_bgp_summary_information
#getNotOperationalBGP = dev.rpc.get_bgp_summary_information(table !='Established')
print(getOperationalBGP)




dev.close()
