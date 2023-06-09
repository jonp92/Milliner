from ._anvil_designer import SettingsTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .AppUsers import AppUsers
from .. import Startup

class Settings(SettingsTemplate):
  def __init__(self, **properties):
    self.users = anvil.server.call('get_app_users_table').search()
    self.url = Startup.url
    self.api_key = Startup.api_key
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_save_click(self, **event_args):
    """This method is called when the button is clicked"""
    if app_tables.settings.get() == None:
      app_tables.settings.add_row(url=self.url, api_key=self.api_key)
      self.refresh_data_bindings()
    else:
      settings_row = app_tables.settings.get()
      settings_row.update(url=self.text_box_url.text, api_key=self.text_box_api_key.text)
      self.refresh_data_bindings()
      
  def button_test_api_click(self, **event_args):
    """This method is called when the button is clicked"""
    try:
      status_returned = anvil.server.call('test_api_key', url=self.url, api_key=self.api_key)
    except:
      raise Exception('No URL has been saved in Settings')
    if status_returned == 200:
      status = f'{status_returned} - Connection Succesful'
    else:
      status = f'Unable to connect - {status_returned}. Please check your API key, URL, and CORS headers'
    alert(status, title="API Test Results")

  def button_app_users_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.clear()
    self.add_component(AppUsers())

  def button_renew_api_key_click(self, **event_args):
    """This method is called when the button is clicked"""
    result, response, new_api_key = anvil.server.call('renew_api_key', url=self.url, api_key=self.api_key)
    if result == True and response == 'Key updated and validated':
      anvil.server.call('update_api_key_settings', new_api_key)
      self.api_key = [r['api_key'] for r in app_tables.settings.search()][0]
      Notification(response, timeout=3).show()
    elif result == True:
      Notification(response, timeout=3).show()
    elif result == False:
      Notification(response, timeout=3).show()


      
    

