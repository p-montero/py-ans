#!/usr/bin/env python
'''
Remove the two objects created in exercise #3 from the database.
DISCLAIMER NOTE: Solution is limited to the exercise's scope
'''

from net_system.models import NetworkDevice
import django
from termcolor import colored

def main():
    Record_Exist = False
# Delete the 2 NOKIA routers added in exercise 3
    django.setup()
    pynet_rtr3 = NetworkDevice.objects.get(device_name='pynet-rtr3')
    pynet_rtr4 = NetworkDevice.objects.get(device_name='pynet-rtr4')
    pynet_rtr3.delete()
    pynet_rtr4.delete()

    # Print -- device : device_type ONLY IF the devices were not deleted
    print "\n Are [pynet_rtr3] and [pynet_rtr4] devices still in the database ... \n"
    pylab_devices = NetworkDevice.objects.all()
    for a_device in pylab_devices:
        if 'nokia' in a_device.device_type:
          print "-- " + colored(a_device, 'blue') + " : " + colored(a_device.device_type, 'green') + "\n"
          Record_Exist = True
    if not Record_Exist:
          print " [pynet_rtr3] and [pynet_rtr4] were effectively DELETED from the database"

if __name__ == "__main__":
    main()
