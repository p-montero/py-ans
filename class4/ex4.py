#!/usr/bin/env python
'''
Use PExpect to change the logging buffer size (logging buffered <size>) on pynet-rtr2.
Verify this change by examining the output of 'show run'.

The username and password for pynet-rtr1, pynet-rtr2, and for the juniper-srx are:
username: pyclass
password: 88newclass

NOTE: Solution is limited to the exercise's scope
'''

import pexpect
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
    print "Establishing an SSH session to "+colored(rtr2_ip, 'blue')
    print "**********************************"
    rem_conn_ssh = pexpect.spawn('ssh -l {} {} -p {}'.format(username, rtr2_ip, port))
    rem_conn_ssh.timeout = 10
    #print "Establishing an SSH session to %s", % rtr2_ip
    " Match ssword:"
    rem_conn_ssh.expect('ssword:')
    " Local connection to pylab using sshutle vpn and take few seconds ..."
    rem_conn_ssh.sendline(passwd)
    " Match prompt after sucessful password"
    rem_conn_ssh.expect('#')
    time.sleep(1)
    " Sending commands "
    " Pagination OFF Cisco IOS"
    rem_conn_ssh.sendline('terminal length 0')
    rem_conn_ssh.expect('#')
    " Configuration mode"
    rem_conn_ssh.sendline('configure t')
    rem_conn_ssh.expect('#')
    rem_conn_ssh.sendline('logging buffered 32768')
    rem_conn_ssh.expect('#')
    rem_conn_ssh.sendline('end')
    rem_conn_ssh.expect('#')
    rem_conn_ssh.sendline('show run | i logging b')
    rem_conn_ssh.expect('#')
    time.sleep(1)
    print "Output to <show run | i logging b> ... \n"
    print rem_conn_ssh.before

if __name__ == "__main__":
    main()
