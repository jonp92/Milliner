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
    self.drop_down_1.items = [r['name'] for r in anvil.server.call('get_hs_users_table').search()]

    # Any code you write here will run before the form opens.

  def button_add_machine_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.column_panel_add_machine.visible = True


