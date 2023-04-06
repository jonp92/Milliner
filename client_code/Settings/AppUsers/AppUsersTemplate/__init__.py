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
    print(self.text_box_password.text)
    if self.text_box_password.text == '':
      anvil.server.call('update_app_user', self.text_box_email.text, self.item, False, None)
    else:
      anvil.server.call('update_app_user', self.text_box_email.text, self.item, True, self.text_box_password.text)
    self.parent.raise_event('x-refresh')
    self.data_row_panel_view.visible = True
    self.data_row_panel_edit.visible = False

  def button_delete_user_click(self, **event_args):
    """This method is called when the button is clicked"""
    delete_user = alert('Are you SURE you want to DELETE ' + self.item['email'], buttons=[('Yes', True), ('No', False)])
    if delete_user:
      with Notification('Deleted User ' + self.item['email'], style='info'):
        self.item.delete()
        self.parent.raise_event('x-refresh')






