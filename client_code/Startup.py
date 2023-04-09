import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#

user = anvil.users.login_with_form()
version = 'v.0.1.3'

fresh_install = anvil.server.call('check_fresh_install')
if not fresh_install['settings_exists']:
    url = ''
    api_key = ''
    sync_time = 'Never Synced'
elif fresh_install['settings_exists']:
    url = [r['url'] for r in app_tables.settings.search()][0]
    api_key = [r['api_key'] for r in app_tables.settings.search()][0]
    sync_time = [r['last_hs_sync'] for r in app_tables.settings.search()][0]

anvil.open_form('Home')