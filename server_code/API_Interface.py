import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import requests



@anvil.server.callable
def test_api_key(url, api_key):
    response = requests.get(
        str(url)+"/api/v1/apikey",
        headers={
            'Accept': 'application/json',
            'Authorization': 'Bearer '+str(api_key)
        }
    )
    return response.status_code

@anvil.server.callable
  def