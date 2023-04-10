from ._anvil_designer import MachineDetailTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import Startup

class MachineDetail(MachineDetailTemplate):
  def __init__(self, id, machine_row, **properties):
    # Set Form properties and Data Bindings.
    self.url = Startup.url
    self.api_key = Startup.api_key
    self.item = anvil.server.call('get_machine_routes', self.url, self.api_key, id)
    self.machine = machine_row
    self.init_components(**properties)
    if self.item == {'routes': []}:
      self.column_panel_routes_container.clear()
      self.column_panel_routes_container.add_component(Label(text='This machine does not have any routes registered in Headscale.'))      
      self.drop_down_users.items = [r['name'] for r in anvil.server.call('get_hs_users_table').search()]
      self.drop_down_users.selected_value = self.machine['user']
    else:
      self.repeating_panel_machine_routes.items = self.item['routes']
      self.drop_down_users.items = [r['name'] for r in anvil.server.call('get_hs_users_table').search()]
      self.drop_down_users.selected_value = self.machine['user']
    # Any code you write here will run before the form opens.
  
  def button_update_machine_settings_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.raise_event("x-close-alert", value=True)
    if self.text_box_machine_name.tag == True:
      anvil.server.call('rename_machine', self.url, self.api_key, self.machine['id'], self.text_box_machine_name.text)
      anvil.server.call('move_user', self.url, self. api_key, self.machine['id'], self.drop_down_users.selected_value)
    else:
      anvil.server.call('move_user', self.url, self. api_key, self.machine['id'], self.drop_down_users.selected_value)
      
  def text_box_machine_name_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.text_box_machine_name.tag = True

  def button_delete_machine_click(self, **event_args):
    """This method is called when the button is clicked"""
    answer = confirm('Are you sure you want to delete ' + self.machine['givenName'])
    if answer:
      anvil.server.call('delete_machine', self.url, self.api_key, self.machine['id'])
      self.machine.delete()
      self.raise_event("x-close-alert", value=True)



