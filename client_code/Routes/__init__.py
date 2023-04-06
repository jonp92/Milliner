from ._anvil_designer import RoutesTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Routes(RoutesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.item = anvil.server.call('get_routes_table')
    self.init_components(**properties)
    self.repeating_panel_machines.items = self.item.search()
    # Any code you write here will run before the form opens.
