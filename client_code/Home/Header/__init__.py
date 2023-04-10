from ._anvil_designer import HeaderTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import Startup

class Header(HeaderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.user = Startup.user
    if self.user:
      self.link_user.text = self.user['email']
    else:
      self.link_user.text = 'None'
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_user_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.users.configure_account_with_form()

  def button_sign_out_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().column_panel_home.clear()
    anvil.users.logout()
    anvil.users.login_with_form()
    open_form('Home')
    
    
    
    


