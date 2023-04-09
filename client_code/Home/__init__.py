from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Machines import Machines
from ..Users import Users
from ..Routes import Routes
from ..Settings import Settings
from .. import Startup

class Home(HomeTemplate):
  def __init__(self, **properties):
    if app_tables.settings.get():
      self.label_sync_time.text = [r['last_hs_sync'] for r in app_tables.settings.search()][0]
    else:
      self.label_sync_time.text = 'Never Synced'
    self.item = anvil.server.call('get_machine_table').search(online=True)
    self.version = Startup.version
    self.url = Startup.url
    self.api_key = Startup.api_key
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    
    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    if self.url == "":
      alert('No URL has been set. The application will not function until one is set in Settings.', title='No URL!')
    if self.api_key == "":
      alert('No API Key has been set. The application will not function until one is set in Settings.', title='No API Key!')  

  def link_machines_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.column_panel_home.clear()
    self.column_panel_home.add_component(Machines(), full_width_row=True)

  def link_users_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.column_panel_home.clear()
    self.column_panel_home.add_component(Users())

  def link_user_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.users.configure_account_with_form()

  def image_logo_mouse_down(self, x, y, button, **event_args):
    """This method is called when a mouse button is pressed on this component"""
    open_form('Home')    

  def link_home_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Home')

  def link_routes_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.column_panel_home.clear()
    self.column_panel_home.add_component(Routes())

  def link_settings_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.column_panel_home.clear()
    self.column_panel_home.add_component(Settings())

  def button_refresh_data_click(self, **event_args):
    """This method is called when the button is clicked"""
    with Notification('Refreshing Data from Headscale'):
      anvil.server.call('record_users')
      anvil.server.call('record_machines')
      anvil.server.call('record_routes')
      self.item = anvil.server.call('get_machine_table').search(online=True)
      self.label_sync_time.text = [r['last_hs_sync'] for r in app_tables.settings.search()][0]

  def button_test_function_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert(anvil.server.call('get_api_key_info', self.url, self.api_key))








    




    

