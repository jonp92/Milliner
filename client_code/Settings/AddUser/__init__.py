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
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_save_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('add_appuser', self.text_box_email.text, self.check_box_enabled.checked, True, self.text_box_password.text)
    Notification(f'User: {self.text_box_email.text} added successfully').show()
    self.parent.raise_event('x-refresh')

