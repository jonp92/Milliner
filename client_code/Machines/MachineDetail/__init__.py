from ._anvil_designer import MachineDetailTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class MachineDetail(MachineDetailTemplate):
  def __init__(self, id, **properties):
    # Set Form properties and Data Bindings.
    self.url = [r['url'] for r in app_tables.settings.search()][0]
    self.api_key = [r['api_key'] for r in app_tables.settings.search()][0]
    self.item = anvil.server.call('get_machine_routes', self.url, self.api_key, id)
    self.init_components(**properties)
    print(self.item)
    if self.item == {'routes': []}:
      self.clear()
      self.add_component(Label(text='No Registered Routes for this Device'))
    else:
      self.repeating_panel_machine_routes.items = self.item['routes']
    # Any code you write here will run before the form opens.
