from __future__ import print_function

import os

from vconnector.core import VConnector
from vconnector.core import VConnectorDatabase
from vpoller.log import logger
from vpoller.exceptions import VPollerException

DEFAULT_PATH = '/var/lib/vconnector/vconnector.db'

def create_agents(self, db_path=DEFAULT_PATH):
    logger.debug('Creating vSphere Agents')
    db = VConnectorDatabase(self.config.get('db_path'))
    agents = db.get_agents(only_enabled=True)

    if not agents:
        logger.warning('No registered or enabled vSphere Agents found')
        raise VPollerException(
            'No registered or enabled vSphere Agents found'
        )

    for agent in agents:
        a = VConnector(
            user=agent['user'],
            pwd=agent['pwd'],
            host=agent['host'],
            cache_enabled=self.config.get('cache_enabled'),
            cache_maxsize=self.config.get('cache_maxsize'),
            cache_ttl=self.config.get('cache_ttl'),
            cache_housekeeping=self.config.get('cache_housekeeping')
        )
        self.agents[a.host] = a
        logger.info('Created vSphere Agent for %s', agent['host'])
    
    client = VConnector(
        agent['user'],
        agent['pwd'],
        agent['host']
    )

