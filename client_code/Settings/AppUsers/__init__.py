from ._anvil_designer import AppUsersTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class AppUsers(AppUsersTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_edit_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.data_row_panel_view.visible = False
    self.data_row_panel_edit.visible = True

  def button_save_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('update_app_user', self.text_box_email.text, self.item)
    self.parent.raise_event('x-refresh')
    self.data_row_panel_view.visible = True
    self.data_row_panel_edit.visible = False



