# -*- coding: utf-8 -*-
'''
    :codeauthor: David Boucha
    :copyright: © 2013 by the SaltStack Team, see AUTHORS for more details.
    :license: Apache 2.0, see LICENSE for more details.


    salt.grains.external_ip
    ~~~~~~~~~~~~~~~~~~~~~~~

    Return the external IP address reported by boucha.saltstack.com
'''

# Import Python Libs
import requests
from pprint import pprint

# Import salt libs
from salt.utils.validate.net import ipv4_addr as _ipv4_addr

# Import errors
from requests.exceptions import Timeout, ConnectionError, HTTPError


def external_ip():
    '''
    Return the external IP address
    '''
    check_url = 'http://boucha.saltstack.com:8080'
    __opts__ = {}

    if __opts__.get('request_external_ip', True):
        try:
            r = requests.get(check_url, timeout=0.1)
            ip_addr = r.json()
            pprint(ip_addr)
            return {'external_ip': ip_addr['ip_addr']}
        except Timeout as exc:
            print('Timeout exceeded: {0}'.format(exc))
        except (ConnectionError, HTTPError) as exc:
            print('Connection error: {0}'.format(exc))

    return {'external_ip': None}


#external_ip()
