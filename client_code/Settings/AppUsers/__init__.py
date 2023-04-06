from ._anvil_designer import AppUsersTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from ..AddUser import AddUser
from anvil.tables import app_tables

class AppUsers(AppUsersTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.users = {}
    self.item = anvil.server.call('get_app_users_table').search()
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.

  def button_add_user_click(self, **event_args):
    """This method is called when the button is clicked"""
    save = alert(AddUser(item=self.users), buttons=[('Save', True), ('Cancel', False)], large=True)
    if save:
      anvil.server.call('add_appuser', self.users['email'], self.users['enabled'], True, self.users['password'])
      self.refresh_data_bindings()

