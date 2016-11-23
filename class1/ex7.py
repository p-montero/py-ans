#!/usr/bin/env python
'''
Write a Python program that reads both the YAML file and the JSON file created
in exercise6 and pretty prints the data structure that is returned.
'''

import yaml
import json
import pprint

yfile = 'class1_ex6.yml'
jfile = 'class1_ex6.json'

with open(yfile) as f:
    yaml_l1 = yaml.load(f)

with open(jfile) as f:
    json_l1 = json.load(f)

print '\n'
print '======================='
print ' YAML DATA STRUCTURE   '
print '======================='
print '\n'
pprint.pprint(yaml_l1)
print '\n'
print '======================='
print ' JSON DATA STRUCTURE   '
print '======================='
print '\n'
pprint.pprint(json_l1)
