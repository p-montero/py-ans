#!/usr/bin/env python
'''
Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2) and prints out both the MIB2 sysName and sysDescr.

Per Cisco SNMP Object Navigator
http://snmp.cloudapps.cisco.com/Support/SNMP/do/BrowseOID.do?local=en&substep=2&translate=Translate&tree=NO
sysDescr.0
http://snmp.cloudapps.cisco.com/Support/SNMP/do/BrowseOID.do?local=en&translate=Translate&objectInput=1.3.6.1.2.1.1.1#oidContent
sysName.0
http://snmp.cloudapps.cisco.com/Support/SNMP/do/BrowseOID.do?local=en&translate=Translate&objectInput=1.3.6.1.2.1.1.5#oidContent
These are scalar types and end in .0

Using snmpget/v2:

pmontero@akai:[~]$ snmpget -v2c -c galileo 184.105.247.70 sysName.0
SNMPv2-MIB::sysName.0 = STRING: pynet-rtr1-cats.twb-tech.com

pmontero@akai:[~]$ snmpget -v2c -c galileo 184.105.247.70 sysDescr.0
SNMPv2-MIB::sysDescr.0 = STRING: Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.4(2)T1, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2014 by Cisco Systems, Inc.
Compiled Thu 26-Jun-14 14:15 by prod_rel_team

NOTE: Solution is limited to the exercise's scope
'''

#import snmp_helper
from snmp_helper import snmp_get_oid,snmp_extract
# from pprint import pprint as pp
'''
Using termcolor for some terminal colors - Not required but learning.
'''
from termcolor import colored

# Variables definition
sysDescr = '1.3.6.1.2.1.1.1.0'
# sysDescr = 'sysDescr.0'
sysName = '1.3.6.1.2.1.1.1.0'
# sysName = 'sysName.0'
'''
This version allows to input the IP & snmp_community values
'''
# rtr1_ip = "184.105.247.70"
# rtr2_ip = "184.105.247.71"
# snmp_comm = 'galileo'
snmp_port = 161

def main():
    " Main function definition"
#
    " Creating snmp_devices tuples as defined by snmp_helper"
    rtr1_ip = raw_input("Enter the rtr1 ip address: ")
    rtr2_ip = raw_input("Enter the rtr2 ip address: ")
    snmp_comm = raw_input("Type the snmp_community: ")
    pynet_rtr1 = (rtr1_ip, snmp_comm, snmp_port)
    pynet_rtr2 = (rtr2_ip, snmp_comm, snmp_port)

    print "\n"
    print "SNMP Information  *********************** \n"
    for snmp_device in (pynet_rtr1, pynet_rtr2):
        print "Communicating with device "+colored(snmp_device, 'red')
        print "\n"
        for OID in (sysDescr, sysName):
            snmp_get = snmp_get_oid(snmp_device, oid=OID)
            snmp_response = snmp_extract(snmp_get)
            print colored(snmp_response, 'blue')
        print "\n"
    print "***************************************** \n"

if __name__ == "__main__":
    main()
