#!/usr/bin/env python
'''
Write a script that connects using telnet to the pynet-rtr1 router. Execute the 'show ip int brief' command on the router and return the output.
Try to do this on your own (i.e. do not copy what I did previously). You should be able to do this by using the following items:

telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
rem_conn.read_until(<string_pattern>, TELNET_TIMEOUT)
rem_conn.read_very_eager()
rem_conn.write(<command> + '\n')
rem_conn.close()

NOTE: Solution is limited to the exercise's scope
'''

import telnetlib
import sys
import socket
import time
# from pprint import pprint as pp
'''
Using termcolor for some terminal colors - Not required but learning.
'''
from termcolor import colored

# Variable definition
telnet_port = 23
telnet_timeout = 5
ip_address = "184.105.247.70"
username = "pyclass"
password = "88newclass"

def telnet_conn(ip_address):
    "Opening telnet session"
    try:
        return telnetlib.Telnet(ip_address, telnet_port, telnet_timeout)
    except socket.timeout:
        sys.exit("Telnet connection timed out after "+telnet_timeout+" seconds")

def login(rem_conn, username, password):
    " Login to device "
    # output = rem_conn.read_until("rname:", telnet_timeout)
    rem_conn.read_until("rname:", telnet_timeout)
    rem_conn.write(username + '\n')
    # output += rem_conn.read_until("ssword:", telnet_timeout)
    rem_conn.read_until("ssword:", telnet_timeout)
    rem_conn.write(password + '\n')
    # return output

def send_command(rem_conn, command):
    " Send CLI command "
    " trailing characters removed using rstrip"
    command = command.rstrip()
    rem_conn.write(command + '\n')
    time.sleep(3)
    return rem_conn.read_very_eager()

def main():
    " Main function definition"
#   print colored("Connecting to router with IP: "+ip_address+" ...", 'blue')
    print "Connecting to router with IP: "+colored(ip_address, 'red')+" ..."
    rem_conn = telnet_conn(ip_address)
    print "Passing username and password ..."
    print "OUTPUT >> "
    login(rem_conn, username, password)

    time.sleep(3)
    rem_conn.read_very_eager()
    output = send_command(rem_conn, 'show ip int brief')

    print output

    rem_conn.close()

if __name__ == "__main__":
    main()
