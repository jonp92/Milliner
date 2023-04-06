from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Home(HomeTemplate):
  def __init__(self, **properties):
    if anvil.users.get_user():
      pass
    else:
      anvil.users.login_with_form()
      self.url = [r['url'] for r in app_tables.settings.search()][0]
      self.api_key = [r['api_key'] for r in app_tables.api_keys.search()][0]
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""

  def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    print(anvil.server.call('get_machines', self.url, self.api_key))



    

