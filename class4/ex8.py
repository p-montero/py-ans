#!/usr/bin/env python
'''
Use Netmiko to change the logging buffer size (logging buffered <size>) and to disable console logging
(no logging console) from a file on both pynet-rtr1 and pynet-rtr2 (see 'Errata and Other Info, item #4).

# logging buffered 65536
# no logging console
> included on file: class4.cfg

The username and password for pynet-rtr1, pynet-rtr2, and for the juniper-srx are:
username: pyclass
password: 88newclass

NOTE: Solution is limited to the exercise's scope
'''

from netmiko import ConnectHandler
# from getpass import getpass as gp
from ne import rtr1, rtr2
from pprint import pprint as pp
'''
Using termcolor for some terminal colors - Not required but learning.
'''
from termcolor import colored
import time

" Devices dictionaries defined in class4.cfg"

def main():
    " Main function definition"
#
    for ne in (rtr1, rtr2):
        " Opening SSH connection "
        print "Establishing an SSH session to Network Element: "+colored(ne['ip'], 'blue')+" : "+colored(ne['port'], 'green')
        print "**********************************"

        rem_conn_ssh = ConnectHandler(**ne)
        output = rem_conn_ssh.send_config_from_file(config_file='class4.cfg')
        print "Output to <show run | i logging> ... \n"
        output = rem_conn_ssh.send_command("show run | i logging")
        print output
        print "\n"

if __name__ == "__main__":
    main()
