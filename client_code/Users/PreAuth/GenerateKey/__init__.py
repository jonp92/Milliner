from ._anvil_designer import GenerateKeyTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class GenerateKey(GenerateKeyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings
    self.init_components(**properties)
    self.drop_down_users.items = [r['name'] for r in anvil.server.call('get_hs_users_table').search()]

    # Any code you write here will run before the form opens.

  def check_box_ephmeral_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if self.check_box_ephmeral.checked:
      self.item['is_ephemeral'] = 'True'
    else:
      self.item['is_ephemeral'] = 'False'

  #def check_box_reusable_change(self, **event_args):
   # """This method is called when this checkbox is checked or unchecked"""
    #if self.check_box_reusable.checked:
      #self.item['is_reusable'] = 'True'
    #else:
      #self.item['is_reusable'] = 'False'




