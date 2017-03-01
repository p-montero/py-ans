#!/usr/bin/env python
'''
Use Netmiko to connect to each of the devices in the database. Execute 'show version' on each device.
Record the amount of time required to do this.
DISCLAIMER NOTE: Solution is limited to the exercise's scope
'''

from net_system.models import NetworkDevice
import django
from termcolor import colored
from datetime import datetime
from netmiko import ConnectHandler

def sh_ver(a_device):
# Execute cmd with NETMIKO
    creds = a_device.credentials
    rem_conn_ssh = ConnectHandler(device_type=a_device.device_type, ip=a_device.ip_address, username=creds.username,
                                 password=creds.password, port=a_device.port, secret='')
    # Output cmd
    output = rem_conn_ssh.send_command_expect("show version")
    print "\n <<--------------------------->> \n "+ colored(output, 'green') + "\n"

def main():
# Main function to connect to the devices using NETMIKO and execute a cmd.
    django.setup()
# Record start time
    start_time = datetime.now()
    pylab_devices = NetworkDevice.objects.all()
    for a_device in pylab_devices:
        sh_ver(a_device)

# Function sh_ver runtime calculation
    runtime = datetime.now() - start_time
    print "This operation required " + colored(runtime, 'red')

if __name__ == "__main__":
    main()
