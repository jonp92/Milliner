from ._anvil_designer import UserRowTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..PreAuth import PreAuth

class UserRow(UserRowTemplate):
  def __init__(self, **properties):
    self.url = [r['url'] for r in app_tables.settings.search()][0]
    self.api_key = [r['api_key'] for r in app_tables.settings.search()][0]
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_cancel_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.data_row_panel_edit.visible = False
    self.data_row_panel_view.visible = True

  def button_update_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def button_delete_user_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('delete_user', self.url, self.api_key, self.item['name'])
    self.item.delete()
    #anvil.server.call('delete_hs_table_row', self.item)
    self.parent.raise_event('x-refresh')

  def link_id_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.data_row_panel_view.visible = False
    self.data_row_panel_edit.visible = True

  def button_preauth_keys_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert(PreAuth(self.label_name.text), large=True)



  


