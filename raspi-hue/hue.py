#!/usr/bin/env python

import os
import sys
import json
import pprint
import nmap

from phue import Bridge

def find_hub(cidr='192.168.0.0/28'):

    PHILIIPS_VENDOR_NAME = 'Philips Lighting BV'

    nm = nmap.PortScanner()
    nm.scan(hosts=cidr, arguments='-sP', sudo=True)

    if len(nm.all_hosts()) == 0:
        print nm['nmap']['scaninfo']['error']

    for host in nm.all_hosts():
        if 'mac' in nm[host]['addresses']:
            if nm[host]['vendor'].itervalues().next() == PHILIIPS_VENDOR_NAME:
                return nm[host]


def get_bridge():

    USER_HOME = 'HOME'

    config_file_path = os.path.join(os.getenv(USER_HOME), '.python_hue')

    if os.path.exists(config_file_path):
        with open(config_file_path) as data_file:
            data = json.load(data_file)
        b = Bridge(data.keys()[0])

    else:
        hub_data = find_hub()
        b = Bridge(hub_data['addresses']['ipv4'])

    b.connect()

    return b

def main(argv):

    pp = pprint.PrettyPrinter(indent=2)

    b = get_bridge()

    bridge_state = b.get_api()

    print "bridge_state"
    pp.pprint(bridge_state)

    # lights = b.lights
    # for l in lights:
    #     print(l.name)

    light_objects = b.get_light_objects('id')
    print "Light objects"
    pp.pprint(light_objects)



if __name__ == "__main__":
    main(sys.argv)
