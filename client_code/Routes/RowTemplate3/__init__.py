from ._anvil_designer import RowTemplate3Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate3(RowTemplate3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def check_box_enabled_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    self.url = [r['url'] for r in app_tables.settings.search()][0]
    self.api_key = [r['api_key'] for r in app_tables.settings.search()][0]
    anvil.server.call('update_route', self.url, self.api_key, self.item['id'], self.check_box_enabled.checked)
    anvil.server.call('record_routes')
    self.refresh_data_bindings()

