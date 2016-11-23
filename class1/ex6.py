#!/usr/bin/env python
'''
Write a Python program that creates a list. One of the elements of the list
should be a dictionary with at least two keys. Write this list out to a file
using both YAML and JSON formats. The YAML file should be in the expanded form.
'''

import yaml
import json

yfile = 'class1_ex6.yml'
jfile = 'class1_ex6.json'

d1 = {
    'hostname': 'CNI3TXMX1CW',
    'model': 'MX480',
    'loopback_ip': '22.2.2.1',
    'snmp_ro': 'public',
}

l1 = ['lab_router', 'austin', d1]

with open(yfile, "w") as f:
    f.write(yaml.dump(l1, default_flow_style=False))

with open(jfile, "w") as f:
    json.dump(l1, f)
