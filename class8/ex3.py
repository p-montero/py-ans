#!/usr/bin/env python
'''
Create two new test NetworkDevices in the database.
Use both direct object creation and the .get_or_create() method to create the devices.
DISCLAIMER NOTE: Solution is limited to the exercise's scope
'''

from net_system.models import NetworkDevice
import django
from termcolor import colored

def main():
# Main function to add 2 new devices in the database
    django.setup()
    '''     2 new Nokia routers added to the db.
            For consistency use the same field order definition found in cat ~/DJANGOX/djproject/net_system/load_devices.py '''
# pynet-rtr3
    pynet_rtr3 = NetworkDevice(
        device_name='pynet-rtr3',
        device_type='nokia_timos',
        ip_address='184.105.247.176',
        port=22,
    )
    pynet_rtr3.save()

# pynet-rtr4
    pynet_rtr4 = NetworkDevice.objects.get_or_create(
        device_name='pynet-rtr4',
        device_type='nokia_timos',
        ip_address='184.105.247.177',
        port=22,
    )

    # Print -- device : device_type ONLY for new added devices
    print "\n NEW added devices to the database ... \n"
    pylab_devices = NetworkDevice.objects.all()
    for a_device in pylab_devices:
        if 'nokia' in a_device.device_type:
          print "-- " + colored(a_device, 'blue') + " : " + colored(a_device.device_type, 'green') + "\n"

if __name__ == "__main__":
    main()
