import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import json


@anvil.server.callable
@anvil.server.background_task
def record_machines():
  import datetime
  now = datetime.datetime.now()
  date_string = now.strftime("%Y-%m-%d")
  time_string =now.strftime("%H:%M:%S")
  url = [r['url'] for r in app_tables.settings.search()][0]
  api_key = [r['api_key'] for r in app_tables.settings.search()][0]
  data=anvil.server.call('get_machines', url, api_key)
  for machine in data['machines']:
    machine_row = app_tables.machines.get(id=machine['id'])
    if machine_row:
      machine_row.update(name=machine['name'], id=machine['id'], ipAddr=machine['ipAddresses'], 
                                online=machine['online'], 
                                user= machine['user']['name'],
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
    settings_row = app_tables.settings.get()
    settings_row.update(last_hs_sync=f'{date_string}-{time_string}')

@anvil.server.callable
@anvil.server.background_task
def record_users():
  url = [r['url'] for r in app_tables.settings.search()][0]
  api_key = [r['api_key'] for r in app_tables.settings.search()][0]
  data = anvil.server.call('get_users', url, api_key)
  for user in data['users']:
    user_row = app_tables.hs_users.get(id=user['id'])
    if user_row:
      user_row.update(id=user['id'], name=user['name'], createdAt=user['createdAt'])
    else:
      app_tables.hs_users.add_row(id=user['id'], name=user['name'], createdAt=user['createdAt'])

@anvil.server.callable
@anvil.server.background_task
def record_routes():
  url = [r['url'] for r in app_tables.settings.search()][0]
  api_key = [r['api_key'] for r in app_tables.settings.search()][0]
  data = anvil.server.call('get_routes', url, api_key)
  for route in data['routes']:
    route_row = app_tables.routes.get(id=int(route['id']))
    if route_row:
      route_row.update(id=int(route['id']), machineName=route['machine']['name'], prefix=route['prefix'], enabled=route['enabled'], machineIPs=route['machine']['ipAddresses'])
    else:
      app_tables.routes.add_row(id=int(route['id']), machineName=route['machine']['name'], prefix=route['prefix'], enabled=route['enabled'], machineIPs=route['machine']['ipAddresses'])
