#!/usr/bin/env python
'''
Use Netmiko to change the logging buffer size (logging buffered <size>) on pynet-rtr2.

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
cmd_lst = ['logging buffered 16384']

def main():
    " Main function definition"
#
    " Opening SSH connection"
    print "Establishing an SSH session to Network Element: "+colored(rtr2['ip'], 'blue')+" : "+colored(rtr2['port'], 'green')
    print "**********************************"

    rem_conn_ssh = ConnectHandler(**rtr2)
    rem_conn_ssh.send_config_set(cmd_lst)

    print "Output to <show run | i logging b> ... \n"
    output = rem_conn_ssh.send_command("show run | i logging b")
    print output

if __name__ == "__main__":
    main()
