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

class Home(HomeTemplate):
  def __init__(self, **properties):
    self.version = 'v.0.0.3'
    self.url = [r['url'] for r in app_tables.settings.search()][0]
    
    self.api_key = [r['api_key'] for r in app_tables.api_keys.search()][0]
    self.user = anvil.users.get_user()
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.visible = False
    if self.user:
      self.visible = True
    else:
      anvil.users.login_with_form()
      self.visible = True
    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""

  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    if self.url == "":
      alert('No URL has been set. The application will not function until one is set in Settings.', title='No URL!')
    if self.api_key == "":
      alert('No API Key has been set. The application will not function until one is set in Settings.', title='No API Key!')  

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert(anvil.server.call('test_api_key', self.url, self.api_key))

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





    




    

