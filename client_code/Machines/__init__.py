from ._anvil_designer import MachinesTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import Startup

class Machines(MachinesTemplate):
  def __init__(self, **properties):
    self.url = Startup.url
    self.api_key = Startup.api_key
    self.item = anvil.server.call('get_machine_table')
    self.repeating_panel_machines.set_event_handler('x-refresh', self.refresh_data)
    self.init_components(**properties)
    self.repeating_panel_machines.items = self.item.search()    
    self.drop_down_user.items = [r['name'] for r in anvil.server.call('get_hs_users_table').search()]
    # Any code you write here will run before the form opens.

  def refresh_data(self, **event_args):
    anvil.server.call('record_machines')
    self.item = anvil.server.call('get_machine_table')
    self.repeating_panel_machines.items = self.item.search()
    
  def button_add_machine_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.column_panel_add_machine.visible = True

  def button_save_new_machine_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert(anvil.server.call('register_machine', self.url, self.api_key, self.text_box_nodekey.text, self.drop_down_user.selected_value))
    self.refresh_data_bindings()

  def button_cancel_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.column_panel_add_machine.visible = False





    


