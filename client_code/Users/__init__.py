from ._anvil_designer import UsersTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Users(UsersTemplate):
  def __init__(self, **properties):
    self.item = anvil.server.call('get_hs_users_table').search()
    self.init_components(**properties)
    self.repeating_panel_users.set_event_handler('x-refresh', self.refresh_data)
    #self.repeating_panel_users.items = self.item.search()
    # Any code you write here will run before the form opens.

  def refresh_data(self, **event_args):
    self.item = anvil.server.call('get_hs_users_table').search()
    
  def button_save_new_user_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.url = [r['url'] for r in app_tables.settings.search()][0]
    self.api_key = [r['api_key'] for r in app_tables.settings.search()][0]
    user_name = self.text_box_username.text
    json_string = '{"name": "'+user_name+'"}'
    status = anvil.server.call('add_user', self.url, self.api_key, json_string)
    if status == True:
      Notification(f'Username {self.text_box_username.text} added succesfully').show()
      anvil.server.call('record_users')
      self.item = anvil.server.call('get_hs_users_table').search()
      self.column_panel_new_user.visible = False
      self.button_add_user.visible = True
    else:
      Notification('Unable to add user to Headscale').show()
      self.column_panel_new_user.visible = False
      self.button_add_user.visible = True

  def button_add_user_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.button_add_user.visible = False
    self.column_panel_new_user.visible = True

  def button_cancel_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.column_panel_new_user.visible = False
    self.button_add_user.visible = True



