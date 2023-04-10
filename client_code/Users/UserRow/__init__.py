from ._anvil_designer import UserRowTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..PreAuth import PreAuth
from ... import Startup

class UserRow(UserRowTemplate):
  def __init__(self, **properties):
    self.url = Startup.url
    self.api_key = Startup.api_key
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
    form = get_open_form()
    form.column_panel_home.clear()
    form.column_panel_home.add_component(PreAuth(self.label_name.text))
    #alert(PreAuth(self.label_name.text), large=True)



  


