from ._anvil_designer import SettingsTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .AddUser import AddUser

class Settings(SettingsTemplate):
  def __init__(self, **properties):
    self.users = anvil.server.call('get_app_users_table').search()
    self.repeating_panel_app_users.set_event_handler('x-refresh', self.refresh_data)
    if app_tables.settings.get() == None:
      self.item['url'] = ''
      self.item['api_key'] = ''
      self.text_box_url.placeholder = 'Insert your Headscale Server URL'
      self.text_box_api_key.placeholder = 'Insert your Headscale Server API Key'
    else:
      self.item['url'] = [r['url'] for r in app_tables.settings.search()][0]
      self.item['api_key'] = [r['api_key'] for r in app_tables.settings.search()][0]
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def refresh_data(self, **event_args):
    self.repeating_panel_app_users.items = anvil.server.call('get_app_users_table').search()
  def button_save_click(self, **event_args):
    """This method is called when the button is clicked"""
    if app_tables.settings.get() == None:
      app_tables.settings.add_row(url=self.item['url'], api_key=self.item['api_key'])
      self.refresh_data_bindings()
    else:
      settings_row = app_tables.settings.get()
      settings_row.update(url=self.item['url'], api_key=self.item['api_key'])
      self.refresh_data_bindings()
  def button_test_api_click(self, **event_args):
    """This method is called when the button is clicked"""
    status_returned = anvil.server.call('test_api_key', self.item['url'], self.item['api_key'])
    if status_returned == 200:
      status = f'{status_returned} - Connection Succesful'
    else:
      status = f'Unable to connect - {status_returned}. Please check your API key, URL, and CORS headers'
    alert(status, title="API Test Results")

  def button_add_user_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert(AddUser(), buttons=[], large=True)

