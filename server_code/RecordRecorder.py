import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import json

@anvil.server.callable
@anvil.server.background_task
def record_machines(url, api_key):
  data=anvil.server.call('get_machines', url, api_key)
  for machine in data['machines']:
    machine_row = app_tables.machines.get(id=machine['id'])
    if machine_row:
      machine_row.update(name=machine['name'], id=machine['id'], ipAddr=machine['ipAddresses'], 
                                online=machine['online'], 
                                user= machine['user'],
                                lastSeen= machine['lastSeen'],
                                expiry= machine['expiry'],
                                registerMethod= machine['registerMethod'],
                                discoKey= machine['discoKey'],
                                createdAt= machine['createdAt'],
                                invalidTags= machine['invalidTags'],
                                validTags= machine['validTags'],
                                machineKey= machine['machineKey'],
                                lastSuccessfulUpdate= machine['lastSuccessfulUpdate'],
                                givenName= machine['givenName'],
                                forcedTags = machine['forcedTags'],
                                nodeKey = machine['nodeKey'],
                                preAuthKey= machine['preAuthKey'])
    else:
      app_tables.machines.add_row(name=machine['name'], id=machine['id'], ipAddr=machine['ipAddresses'], 
                                online=machine['online'], 
                                user= machine['user'],
                                lastSeen= machine['lastSeen'],
                                expiry= machine['expiry'],
                                registerMethod= machine['registerMethod'],
                                discoKey= machine['discoKey'],
                                createdAt= machine['createdAt'],
                                invalidTags= machine['invalidTags'],
                                validTags= machine['validTags'],
                                machineKey= machine['machineKey'],
                                lastSuccessfulUpdate= machine['lastSuccessfulUpdate'],
                                givenName= machine['givenName'],
                                forcedTags = machine['forcedTags'],
                                nodeKey = machine['nodeKey'],
                                preAuthKey= machine['preAuthKey'])      
  
