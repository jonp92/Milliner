from ._anvil_designer import MachineRouteRowTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class MachineRouteRow(MachineRouteRowTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_online.text = self.item['machine']['online']
    # Any code you write here will run before the form opens.
