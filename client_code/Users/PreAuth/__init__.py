from ._anvil_designer import PreAuthTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .GenerateKey import GenerateKey
import json
import datetime

class PreAuth(PreAuthTemplate):
  def __init__(self, user_name, **properties):
    # Set Form properties and Data Bindings.
    self.item['selected_user'] = None
    self.item['is_reusable'] = False
    self.item['is_ephemeral'] = False
    self.item['expiration_date'] = '7'
    self.user_name = user_name
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
      # get the current date and time in UTC format
      now = datetime.datetime.utcnow()  
      # add the input number of days to the current date and time
      future_date = now + datetime.timedelta(days=int(self.item['expiration_date']))  
      # convert the future date to ISO 8601 format with UTC timezone
      iso_date = future_date.replace(microsecond=0).isoformat() + 'Z'
      key_dict = {'user': self.item['selected_user'], 'reusable': self.item['is_reusable'], 'ephemeral': self.item['is_ephemeral'], 'expiration': iso_date}
      json_string = json.dumps(key_dict)
      return_response = anvil.server.call('add_preauth_key', self.url, self.api_key, json_string)
      if return_response['status'] == 'True':
        notification_body = return_response['body']['preAuthKey']['key'] + ' generated for user ' + self.user_name + ' and will expire on ' + return_response['body']['preAuthKey']['expiration']
        notification_title = 'PreAuth Key Generated Successfully'
      else:
        notification_body = 'Unable to Generate a PreAuth key for user ' + self.user_name
        notification_title = 'Error Occurred'
      Notification(notification_body, timeout=6, title=notification_title).show()
      self.response = anvil.server.call('get_preauth_keys', self.url, self.api_key, self.user_name)
      self.repeating_panel_preauth_keys.items = self.response['preAuthKeys']
      
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    selected = self.get_selected_rows()
    for key_rows in selected:
      keys = key_rows.get('key')
      users = key_rows.get('user')
      json_string = '{"user": "'+users+'", "key": "'+keys+'"}'
      anvil.server.call('expire_preauth_key', self.url, self.api_key, json_string)

      

  
