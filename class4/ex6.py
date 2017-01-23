#!/usr/bin/env python
'''
Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.

The username and password for pynet-rtr1, pynet-rtr2, and for the juniper-srx are:
username: pyclass
password: 88newclass

NOTE: Solution is limited to the exercise's scope
'''

from netmiko import ConnectHandler
# from getpass import getpass as gp
from pprint import pprint as pp
'''
Using termcolor for some terminal colors - Not required but learning.
'''
from termcolor import colored
import time

" Devices dictionaries "
rtr1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'password': '88newclass',
    'port': 22,
}
rtr2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': '88newclass',
    'port': 22,
}
srx = {
    'device_type': 'juniper',
    'ip': '184.105.247.76',
    'username': 'pyclass',
    'password': '88newclass',
    'port': 22,
}

def main():
    " Main function definition"
#
    for ne in (rtr1, rtr2, srx):
        " Opening SSH connection "
        print "Establishing an SSH session to Network Element: "+colored(ne['ip'], 'blue')+" : "+colored(ne['port'], 'green')
        print "**********************************"

        rem_conn_ssh = ConnectHandler(**ne)
        output = rem_conn_ssh.send_command("show arp")
#        print "Network Element: {}:{}".format(rem_conn_ssh.ip, rem_conn_ssh.port)
#        print "Network Element: %s:%s" % colored(ne['ip'], 'blue') % colored(ne['port'], 'green')
        print "<< show arp >>"
        print "\n"
        print output

if __name__ == "__main__":
    main()
