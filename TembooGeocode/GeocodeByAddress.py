from temboo.Library.Google.Geocoding import GeocodeByAddress
from temboo.core.session import TembooSession

# Create a session with your Temboo account details
session = TembooSession("accountName", "myFirstApp", "abc123xxxxxxxxxxxxxx")

# Instantiate the Choreo
geocodeByAddressChoreo = GeocodeByAddress(session)

# Get an InputSet object for the Choreo
geocodeByAddressInputs = geocodeByAddressChoreo.new_input_set()

# Execute the Choreo
geocodeByAddressResults = geocodeByAddressChoreo.execute_with_results(geocodeByAddressInputs)

# Print the Choreo outputs
print("Latitude: " + geocodeByAddressResults.get_Latitude())
print("Longitude: " + geocodeByAddressResults.get_Longitude())
print("Response: " + geocodeByAddressResults.get_Response())