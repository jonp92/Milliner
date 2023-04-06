from ._anvil_designer import UsersTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Users(UsersTemplate):
  def __init__(self, **properties):
    self.item = anvil.server.call('get_hs_users_table')
    self.init_components(**properties)
    self.repeating_panel_users.items = self.item.search()

    # Any code you write here will run before the form opens.
