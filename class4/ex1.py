#!/usr/bin/env python
'''
Use Paramiko to retrieve the entire 'show version' output from pynet-rtr2

The username and password for pynet-rtr1, pynet-rtr2, and for the juniper-srx are:
username: pyclass
password: 88newclass

NOTE: Solution is limited to the exercise's scope
'''

import paramiko
# from getpass import getpass as gp
from pprint import pprint as pp
'''
Using termcolor for some terminal colors - Not required but learning.
'''
from termcolor import colored
import time

#rtr1_ip = "184.105.247.70"
rtr2_ip = "184.105.247.71"
username = 'pyclass'
passwd = '88newclass'
port = 22

def main():
    " Main function definition"
#
    " Opening SSH connection"
    rem_conn_ssh = paramiko.SSHClient()
    rem_conn_ssh.load_system_host_keys()
    rem_conn_ssh.connect(rtr2_ip, port=port, username=username, password=passwd, look_for_keys=False, allow_agent=False)
    " Start an interactive shell session on the SSH server"
    rem_conn = rem_conn_ssh.invoke_shell()
    #print "Establishing an SSH session to %s", % rtr2_ip
    print "Establishing an SSH session to "+colored(rtr2_ip, 'blue')
    print "\n"
    print "**********************************"
    time.sleep(3)
    " Sending commands "
    " Pagination OFF Cisco IOS"
    rem_conn.send("terminal length 0\n")
    time.sleep(2)
    output = rem_conn.send("show version\n")
    print "Issuing <show version> \n"
    print output
    print "\n END"

if __name__ == "__main__":
    main()
