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
def update_app_user(email, item, password):
  import bcrypt
  # converting password to array of bytes
  bytes = password.encode('utf-8')
  # generating the salt
  salt = bcrypt.gensalt()
  # Hashing the password
  password_hash = bcrypt.hashpw(bytes, salt)
  appuser_row = app_tables.users.get_by_id(item.get_id())
  appuser_row.update(email=email)

@anvil.server.callable
def edit_user(id, first_name, last_name, email, role, enabled, confirmed_email, password):
  import bcrypt
  # converting password to array of bytes
  bytes = password.encode('utf-8')
  # generating the salt
  salt = bcrypt.gensalt()
  # Hashing the password
  password_hash = bcrypt.hashpw(bytes, salt)
  user_row = app_tables.users.get_by_id(id)
  user_row.update(first_name=first_name, last_name = last_name, email = email, role = role, enabled = enabled, confirmed_email = confirmed_email, password_hash = password_hash.decode('utf-8'))

@anvil.server.callable
def add_user(first_name, last_name, email, role, enabled, confirmed_email, password):
  import bcrypt
  # converting password to array of bytes
  bytes = password.encode('utf-8')
  # generating the salt
  salt = bcrypt.gensalt()
  # Hashing the password
  password_hash = bcrypt.hashpw(bytes, salt)
  app_tables.users.add_row(first_name=first_name, last_name=last_name, email=email, role=role, enabled=enabled, confirmed_email=confirmed_email, password_hash=password_hash.decode('utf-8'))
  