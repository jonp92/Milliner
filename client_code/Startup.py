import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import open_form
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#
def fresh_install():
  fresh_install = anvil.server.call('check_fresh_install')
  if not fresh_install['settings_exists']:
      url = ''
      api_key = ''
      return url, api_key
  elif fresh_install['settings_exists']:
      url = [r['url'] for r in app_tables.settings.search()][0]
      api_key = [r['api_key'] for r in app_tables.settings.search()][0]
      return url, api_key
version = 'v.0.1.3'
url, api_key = fresh_install()
def startup():
  user = anvil.users.login_with_form()
  
  open_form('Home')
  return url, api_key
  

if __name__ == "__main__":
 startup()

