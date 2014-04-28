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
import logging
import requests
from pprint import pprint

# Import salt libs
from salt.utils.validate.net import ipv4_addr as _ipv4_addr

# Import errors
from requests.exceptions import Timeout, ConnectionError, HTTPError

log = logging.getLogger(__name__)

def external_ip():
    '''
    Return the external IP address
    '''
    check_url = 'http://boucha.saltstack.com:8080'

    if __opts__.get('request_external_ip', False):
        try:
            r = requests.get(check_url, timeout=0.1)
            ip_addr = r.json()
            return {'external_ip': ip_addr['ip_addr']}
        except Timeout as exc:
            log.debug('Timeout exceeded: {0}'.format(exc))
        except (ConnectionError, HTTPError) as exc:
            log.debug('Connection error: {0}'.format(exc))

    return {'external_ip': None}
