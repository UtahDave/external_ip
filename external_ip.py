# -*- coding: utf-8 -*-
'''
    :codeauthor: David Boucha
    :copyright: © 2013 by the SaltStack Team, see AUTHORS for more details.
    :license: Apache 2.0, see LICENSE for more details.


    salt.grains.external_ip
    ~~~~~~~~~~~~~~~~~~~~~~~

    Return the external IP address reported by an IP reporting service.
    SaltStack provides this at http://boucha.saltstack.com:8080

    The following config item is mandatory to opt in

        external_ip.server: 'http://boucha.saltstack.com:8080'

    The following minion config items are optional:

        external_ip.timeout: 0.5
'''

# Import Python Libs
import logging
import requests

# Import salt libs
from salt.utils.validate.net import ipv4_addr as _ipv4_addr

# Import errors
from requests.exceptions import Timeout, ConnectionError, HTTPError

log = logging.getLogger(__name__)

def external_ip():
    '''
    Return the external IP address
    '''
    check_url = __opts__.get('external_ip.server', False)
    if check_url:
        try:
            timeout = __opts__.get('external_ip.timeout', 0.5)
            r = requests.get(check_url, timeout=timeout)
            ip_addr = r.json()
            if _ipv4_addr(ip_addr['ip_addr']):
                return {'external_ip': ip_addr['ip_addr']}
        except Timeout as exc:
            log.debug('Timeout exceeded: {0}'.format(exc))
        except (ConnectionError, HTTPError) as exc:
            log.debug('Connection error: {0}'.format(exc))

    return {'external_ip': None}
