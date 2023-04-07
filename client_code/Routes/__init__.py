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
    self.item = anvil.server.call('get_routes_tables')
    self.init_components(**properties)
    self.repeating_panel_routes.add_event_handler('x-refresh', self.refresh_data)
    self.repeating_panel_routes.items = self.item.search()
    print(self.item.search()[0])
    # Any code you write here will run before the form opens.

  def refresh_data(self, **event_args):
    self.refresh_data_bindings()
    self.repeating_panel_routes.items = self.item.search()
    