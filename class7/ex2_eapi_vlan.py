#!/usr/bin/env python
'''
Using Arista's pyeapi, create a script that allows you to add a VLAN (both the
VLAN ID and the VLAN name).  Your script should first check that the VLAN ID is
available and only add the VLAN if it doesn't already exist.  Use VLAN IDs
between 100 and 999.  You should be able to call the script from the command
line as follows:
   python eapi_vlan.py --name blue 100     # add VLAN100, name blue
If you call the script with the --remove option, the VLAN will be removed.
   python eapi_vlan.py --remove 100          # remove VLAN100

Once again only remove the VLAN if it exists on the switch.  You will probably
want to use Python's argparse to accomplish the argument processing.

Python's argparse
https://pymotw.com/2/argparse/?__s=67h37xspax7tbibb1vdq

DISCLAIMER NOTE: Solution is limited to the exercise's scope
'''

import pyeapi
import argparse
from termcolor import colored
import pprint

# Function if_vlan using <node> and <vlan_id>, no need to check name
def if_vlan(node, vlan_id):
    vlan_id = str(vlan_id)
    cli_show_vlan_id = 'show vlan id {}'.format(vlan_id)
    # try: if vlan exist, referenced from kbyers lecture/exercise
    try:
        response = node.enable(cli_show_vlan_id)
        if_vlan_result = pyeapi_output(response)['vlans']
        return if_vlan_result[vlan_id]['name']
    except (pyeapi.eapilib.CommandError, KeyError):
        pass

    return False

# Add vlan-id tag in the device, define default name to Unknown if not passed as an argument
# if vlan-id passed as an argument used for the vlan_name
def add_vlan(node, vlan_id, vlan_name=None):
    cli_create_vlan = 'vlan {}'.format(vlan_id)
    cmd_create_vlan = [cli_create_vlan]
    if vlan_name is not None:
        cmd_create_vlan_name = 'name {}'.format(vlan_name)
        cmd_create_vlan.append(cmd_create_vlan_name)
    return node.config(cmd_create_vlan)

# Function to get the result from the list [0]
def pyeapi_output(output):
    return output[0]['result']

def main():
# Open connection using .eapi.conf [pynet-sw3]
# References: https://github.com/arista-eosplus/pyeapi/tree/develop/examples

    node = pyeapi.connect_to("pynet-sw3")

    # Argparse: https://pymotw.com/2/argparse/?__s=67h37xspax7tbibb1vdq
    parser = argparse.ArgumentParser(description="Add/Remove vlan-id from Arista node")
    parser.add_argument("vlan_id", help="VLAN id tag", action="store", type=int)
    parser.add_argument("--name",help="Add VLAN name",action="store",dest="vlan_name",type=str)
    parser.add_argument("--remove", help="Remove the specified VLAN id tag", action="store_true")

    # Variable definition based on the input parsing | Argument Actions
    parsed = parser.parse_args()
    vlan_id = parsed.vlan_id
    vlan_name = parsed.vlan_name
    remove = parsed.remove

    # Argument actions as required by the exercise.

    # Is VLAN id tag configured already?
    # Function if_vlan using <node> and <vlan_id>, no need to check name
    if_vlan_result = if_vlan(node, vlan_id)

    # check if action is remove or add
    if remove:
        if if_vlan_result:
            print "Removing the configured VLAN id tag:" +colored(vlan_id, 'red') + " in the node"
            cli_remove_vlan_id = 'no vlan {}'.format(vlan_id)
            node.config([cli_remove_vlan_id])
        else:
            print "VLAN id tag:" +colored(vlan_id, 'red') + " IS NOT CONFIGURED in the node"
            print "Remove action: FAILED"
    else:
        if if_vlan_result:
            if vlan_name is not None and if_vlan != vlan_name:
                print "VLAN id tag:" +colored(vlan_id, 'yellow') + " found in the node and requiring VLAN id name update"
                add_vlan(node, vlan_id, vlan_name)
            else:
                print "VLAN id tag:" +colored(vlan_id, 'green') + "IS CONFIGURED in the node"
                print "ADD_VLAN action: FAILED"
        else:
            print "VLAN id tag:" +colored(vlan_id, 'green') + " being added into the node ..."
            add_vlan(node, vlan_id, vlan_name)

if __name__ == "__main__":
    main()
