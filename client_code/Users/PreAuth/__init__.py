from ._anvil_designer import PreAuthTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .GenerateKey import GenerateKey

class PreAuth(PreAuthTemplate):
  def __init__(self, user_name, **properties):
    # Set Form properties and Data Bindings.
    self.item['selected_user'] = None
    self.item['is_reusable'] = 'False'
    self.item['is_ephemeral'] = 'False'
    self.item['expiration_date'] = '7'
    self.url = [r['url'] for r in app_tables.settings.search()][0]
    self.api_key = [r['api_key'] for r in app_tables.settings.search()][0]
    self.response = anvil.server.call('get_preauth_keys', self.url, self.api_key, user_name)
    self.repeating_panel_preauth_keys.items = self.response['preAuthKeys']
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def get_selected_rows(self):
      selected = []
      for row_template in self.repeating_panel_preauth_keys.get_components():
        if row_template.check_box_key.checked:
          selected.append(row_template.item)
      return selected

  def button_generate_key_click(self, **event_args):
    """This method is called when the button is clicked"""
    generate_decision = alert(GenerateKey(item=self.item), title='Select a User to generate a new PreAuth key', buttons=[('Ok', True),('Cancel', False)])
    if generate_decision:
      json_string = '{"user": "'+self.item['selected_user']+'", "reusable": "'+self.item['is_reusable']+'", "ephemeral": "'+self.item['is_ephemeral']+'", "expiration": "'+self.item['expiration_date']+'"}'
      Notification(anvil.server.call('add_preauth_key', self.url, self.api_key, json_string), timeout=7).show()
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    selected = self.get_selected_rows()
    for key_rows in selected:
      keys = key_rows.get('key')
      users = key_rows.get('user')
      json_string = '{"user": "'+users+'", "key": "'+keys+'"}'
      anvil.server.call('expire_preauth_key', self.url, self.api_key, json_string)

      

  
