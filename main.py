import data
import helpers

class TestUrbanRoutes:
  @classmethod
  def setup_class(cls):
      if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
          print ("Connected to the Urban Routes server")
      else:
          print ("Cannot connect to Urban Routes. Check the server is on and still running")

  def  test_set_route(self):
       # Add in S8
       print("functioncreated for set route")
       pass

  def test_order_2_ice_creams
      for i in range(2):
          # Add in S8
          print("functioncreated for set route")
          pass