#!/usr/bin/env python
"""
 Update the NetworkDevice objects such that each NetworkDevice links to the correct Credentials.
"""
import django
from net_system.models import NetworkDevice, Credentials
from termcolor import colored

def main():
# Link NE to Credentails identifying vendor, reference the class video where this example is shown
    django.setup()
    pylab_devices = NetworkDevice.objects.all()
    creds = Credentials.objects.all()

    other_creds = creds[0]
    arista_creds = creds[1]

    for a_device in pylab_devices:
        if 'arista' in a_device.device_type:
# OR    if 'pynet-sw' in a_device.device_name:
            a_device.credentials = arista_creds
        else:
            a_device.credentials = other_creds
        a_device.save()

# To print the devices & credentials for verification
    for a_device in pylab_devices:
        print "-- " + colored(a_device, 'blue') + " : " + colored(a_device.credentials, 'green')

if __name__ == "__main__":
    main()
