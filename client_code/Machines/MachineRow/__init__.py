from ._anvil_designer import MachineRowTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..MachineDetail import MachineDetail

class MachineRow(MachineRowTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_machine_id_click(self, **event_args):
    """This method is called when the link is clicked"""
    update = alert(MachineDetail(self.item['id'], self.item), large=True, title=self.item['name'])
    if update:
      self.parent.raise_event('x-refresh')
    




