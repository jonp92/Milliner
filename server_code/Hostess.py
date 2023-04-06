import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_machine_table():
  return app_tables.machines.client_writable_cascade()

@anvil.server.callable
def get_hs_users_table():
  return app_tables.hs_users.client_writable_cascade()

@anvil.server.callable
def get_routes_tables():
  return app_tables.routes.client_writable_cascade()
