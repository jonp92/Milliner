from ._anvil_designer import MachineDetailTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class MachineDetail(MachineDetailTemplate):
  def __init__(self, id, machine_row, **properties):
    # Set Form properties and Data Bindings.
    self.url = [r['url'] for r in app_tables.settings.search()][0]
    self.api_key = [r['api_key'] for r in app_tables.settings.search()][0]
    self.item = anvil.server.call('get_machine_routes', self.url, self.api_key, id)
    self.machine = machine_row
    self.init_components(**properties)
    if self.item == {'routes': []}:
      self.grid_panel_container.clear()
      self.grid_panel_container.add_component(Label(text='This machine does not have any routes registered in Headscale.'))      
      self.drop_down_users.items = [r['name'] for r in anvil.server.call('get_hs_users_table').search()]
      self.drop_down_users.selected_value = self.machine['user']
    else:
      self.repeating_panel_machine_routes.items = self.item['routes']
      self.drop_down_users.items = [r['name'] for r in anvil.server.call('get_hs_users_table').search()]
      self.drop_down_users.selected_value = self.machine['user']
    # Any code you write here will run before the form opens.
