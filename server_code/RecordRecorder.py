import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import json

@anvil.server.callable
def record_machines(url, api_key):
  data=anvil.server.call('get_machines', url, api_key)
  for machine in data['machines']:
    app_tables.machines.add_row(name=machine['name'], id=machine['id'], ipAddr=machine['ipAddresses'])
    print(machine['name'])
    print(machine['id'])
    print(machine['ipAddresses'])
  #app_tables.machines.add_row(data=data)
  
