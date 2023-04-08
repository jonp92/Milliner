from ._anvil_designer import PreAuthTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class PreAuth(PreAuthTemplate):
  def __init__(self, user_name, **properties):
    # Set Form properties and Data Bindings.
    self.url = [r['url'] for r in app_tables.settings.search()][0]
    self.api_key = [r['api_key'] for r in app_tables.settings.search()][0]
    self.response = anvil.server.call('get_preauth_keys', self.url, self.api_key, user_name)
    self.repeating_panel_1.items = self.response['preAuthKeys']
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
