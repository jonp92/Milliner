from ._anvil_designer import RouteRowTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import Startup

class RouteRow(RouteRowTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def check_box_enabled_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    self.url = Startup.url
    self.api_key = Startup.api_key
    anvil.server.call('update_route', self.url, self.api_key, self.item['id'], self.check_box_enabled.checked)
    anvil.server.call('record_routes')
    self.parent.raise_event('x-refresh')

