from ._anvil_designer import AddUserTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class AddUser(AddUserTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.item['email'] = ''
    self.item['password'] = ''
    self.item['enabled'] = ''
    self.init_components(**properties)
    self.check_box_enabled.checked = True
    self.item['enabled'] = True
    

    # Any code you write here will run before the form opens.


