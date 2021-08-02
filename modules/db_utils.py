from __future__ import print_function

import get_agents
import pyVmomi
from vconnector.core import VConnector

def db_connect(self):
    agent = get_agents

    con = VConnector(
        agent['user'],
        agent['pwd'],
        agent['host']
    )

    return con