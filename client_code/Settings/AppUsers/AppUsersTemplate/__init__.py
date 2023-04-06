from ._anvil_designer import AppUsersTemplateTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class AppUsersTemplate(AppUsersTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.set_event_handler('x-refresh-child', self.refresh_data)
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def refresh_data(self, **event_args):
    self.data_row_panel_view.item = self.item
    self.refresh_data_bindings()
    
  def button_edit_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.data_row_panel_view.visible = False
    self.data_row_panel_edit.visible = True

  def button_save_user_edit_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('update_app_user', self.text_box_email.text, self.item, self.text_box_password.text)
    self.parent.raise_event('x-refresh')
    self.refresh_data_bindings()
    self.data_row_panel_view.visible = True
    self.data_row_panel_edit.visible = False





