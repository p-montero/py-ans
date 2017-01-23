#!/usr/bin/env python
'''
Use Netmiko to enter into configuration mode on pynet-rtr2.
Also use Netmiko to verify your state (i.e. that you are currently in configuration mode).

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
rtr2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': '88newclass',
    'port': 22,
}

def main():
    " Main function definition"
#
    " Opening SSH connection"
    print "Establishing an SSH session to "+colored(rtr2['ip'], 'blue')
    print "**********************************"

    rem_conn_ssh = ConnectHandler(**rtr2)
    rem_conn_ssh.config_mode()

    print "Is pynet-rtr2 in <configuration mode> ?"
    output = rem_conn_ssh.check_config_mode()
    print output

if __name__ == "__main__":
    main()
