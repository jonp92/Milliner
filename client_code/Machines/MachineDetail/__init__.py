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
    self.id = id
    self.url = [r['url'] for r in app_tables.settings.search()][0]
    self.api_key = [r['api_key'] for r in app_tables.settings.search()][0]
    self.item = anvil.server.call('get_machine_routes', self.url, self.api_key, id)
    print(self.item)

    self.init_components(**properties)
    #self.label_route_data.text = self.prefixes
    #self.label_advertised_status.text = self.advertised
    #self.label_online_status.text = self.online
    #self.label_enabled_status.text = self.enabled
    # Any code you write here will run before the form opens.
