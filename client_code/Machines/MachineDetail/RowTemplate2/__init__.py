from ._anvil_designer import RowTemplate2Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate2(RowTemplate2Template):
  def __init__(self, **properties):
    self.prefixes = [route['prefix'] for route in self.item['routes']]
    self.advertised = [route['advertised'] for route in self.item['routes']]
    self.online = [route['machine']['online'] for route in self.item['routes']]
    self.enabled = [route['enabled'] for route in self.item['routes']]
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_prefixes.text = self.prefixes
    self.label_advertised.text = self.advertised
    self.label_online.text = self.online
    self.label_enabled.text = self.enabled

    # Any code you write here will run before the form opens.
