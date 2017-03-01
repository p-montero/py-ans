#!/usr/bin/env python
'''
Remove the two objects created in exercise #3 from the database.
DISCLAIMER NOTE: Solution is limited to the exercise's scope
'''

from net_system.models import NetworkDevice
import django
from termcolor import colored

def main():
# Delete the 2 NOKIA routers added in exercise 3
    django.setup()
    try:
        pynet_rtr3 = NetworkDevice.objects.get(device_name='pynet-rtr3')
        pynet_rtr4 = NetworkDevice.objects.get(device_name='pynet-rtr4')
        pynet_rtr3.delete()
        pynet_rtr4.delete()
        print "\n [pynet_rtr3] and [pynet_rtr4] were effectively DELETED from the database"
    except NetworkDevice.DoesNotExist:
        print "\n [pynet_rtr3] and [pynet_rtr4] are not in the database \n"
        pass

# Verification
    print "\n CURRENT DATABASE RECORDS \n"
    pylab_devices = NetworkDevice.objects.all()
    for a_device in pylab_devices:
          print "-- " + colored(a_device, 'blue') + " : " + colored(a_device.device_type, 'green') + "\n"

if __name__ == "__main__":
    main()
