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
    #self.item['enabled'] = True
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_save_click(self, **event_args):
    """This method is called when the button is clicked"""
    Notification(f'User: {self.text_box_email.text} added successfully').show()
    self.raise_event('x-close-alert', value=True)

