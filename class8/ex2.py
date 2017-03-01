#!/usr/bin/env python
'''
Set the vendor field of each NetworkDevice to the appropriate vendor. Save this field to the database.
DISCLAIMER NOTE: Solution is limited to the exercise's scope
'''
from net_system.models import NetworkDevice
import django
from termcolor import colored

def main():
# Main function to update the vendor name base on the device_type : cat load_devices.py | grep device_type
    django.setup()
    pylab_devices = NetworkDevice.objects.all()
    for a_device in pylab_devices:
        if 'juniper' in a_device.device_type:
            a_device.vendor = 'Juniper Networks'
        elif 'arista' in a_device.device_type:
            a_device.vendor = 'Arista Networks'
        elif 'cisco' in a_device.device_type:
            a_device.vendor = 'Cisco Systems'
        a_device.save()

# Print -- device : vendor_name
    for a_device in pylab_devices:
        print "-- " + colored(a_device, 'blue') + " : " + colored(a_device.vendor, 'green')

if __name__ == "__main__":
    main()
