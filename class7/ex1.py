#!/usr/bin/env python
'''
Use Arista's eAPI to obtain 'show interfaces' from the switch.  Parse the 'show interfaces' output to obtain
the 'inOctets' and 'outOctets' fields for each of the interfaces on the switch.  Accomplish this using Arista's pyeapi library.

DISCLAIMER NOTE: Solution is limited to the exercise's scope
'''

import pyeapi
# print "<string> "+colored(variable, 'color')
from termcolor import colored

def main():

# Open connection using .eapi.conf [pynet-sw3]
# References: https://github.com/arista-eosplus/pyeapi/tree/develop/examples

    node = pyeapi.connect_to("pynet-sw3")

    intf = node.enable("show interfaces")
# First item from intf list [0]
    intf = intf[0]
# Use only the result on  intf dictionary
    intf = intf['result']
# Remove all the unneeded information from the dictionary, interfaces
    intf = intf['interfaces']
# Loop through all the interfaces on the node
    print "\n -Interface- \t -inOctects- \t -outOctets- \n"
    for intf_id, intf_key in intf.items():
# u'interfaceCounters':
        intf_Counters = intf_key.get('interfaceCounters', {})
        intf_inOctects = intf_Counters.get('inOctets')
        intf_outOctects = intf_Counters.get('outOctets')
        print colored(intf_id, 'red')+ "\t" + colored(intf_inOctects, 'blue')+ "\t" + colored(intf_outOctects, 'green')

if __name__ == '__main__':
    main()
