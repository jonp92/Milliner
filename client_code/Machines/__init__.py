from ._anvil_designer import MachinesTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Machines(MachinesTemplate):
  def __init__(self, **properties):
    self.item = anvil.server.call('get_machine_table')
    self.init_components(**properties)
    self.repeating_panel_machines.items = self.item.search()

    # Any code you write here will run before the form opens.
