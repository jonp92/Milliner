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

@anvil.server.callable
def check_users_table():
  user = app_tables.users.search()
  if user:
    return False
  else:
    app_tables.users.add_row(confirmed_email=True, email='admin@milliner.login', enabled=True, password_hash='$2y$10$QoAnY4j687bSu/DI/C4n7.Wm2kLIT8fIyCid8406DvqYuBJayaFUK')
    return True

@anvil.server.callable
def get_app_users_table():
  return app_tables.users.client_writable_cascade()

@anvil.server.callable
def update_app_user(email, item):
  appuser_row = app_tables.users.get_by_id(item.get_id())
  appuser_row.update(email=email)
  