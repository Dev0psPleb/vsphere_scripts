from __future__ import print_function

import pyVmomi

from modules import get_agents
from modules import db_utils
from modules.db_utils import db_connect
from vconnector.core import VConnector
from vconnector.core import VConnectorDatabase

client = db_connect()

client.connect()
vms = client.get_vm_view()
print(vms.view)