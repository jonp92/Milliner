import anvil.tables as tables
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
@tables.in_transaction
def check_fresh_install():
  if len(app_tables.users.search()) == 0:
    app_tables.users.add_row(confirmed_email=True, email='admin@milliner.login', enabled=True, password_hash='$2y$10$QoAnY4j687bSu/DI/C4n7.Wm2kLIT8fIyCid8406DvqYuBJayaFUK')
    created_user = True
  else:
    created_user = False
  if len(app_tables.settings.search()) == 0:
    settings_exists = False
  else:
    settings_exists = True
  return {'created_user': created_user, 'settings_exists': settings_exists}
  
@anvil.server.callable
def get_app_users_table():
  return app_tables.users.client_writable_cascade()

@anvil.server.callable
def update_app_user(email, item, pw_update, password):
  appuser_row = app_tables.users.get_by_id(item.get_id())
  if pw_update == False:
    appuser_row.update(email=email)
  elif pw_update == True:
    import bcrypt
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    appuser_row.update(email=email, password_hash=password_hash.decode('utf-8'))

@anvil.server.callable
def add_appuser(email, enabled, confirmed_email, password):
  import bcrypt
  password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
  app_tables.users.add_row(email=email, enabled=enabled, confirmed_email=confirmed_email, password_hash=password_hash.decode('utf-8'))

@anvil.server.callable
def delete_hs_table_row(item):
  item.delete()

@anvil.server.callable
def delete_machine_row(machine_id):
  machine_row = app_tables.machines.get(id=machine_id)
  machine_row.delete()

@anvil.server.callable
def update_api_key_settings(new_api_key):
  app_tables.settings.get().update(api_key=new_api_key)
  
  