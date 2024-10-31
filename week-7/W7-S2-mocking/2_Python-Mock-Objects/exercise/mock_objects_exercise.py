# ----------------------------
# Creating Mock Objects
# ----------------------------

# This script demonstrates how to create and use mock objects in Python 
# using the unittest.mock library. It shows how mock objects can replace 
# actual components in tests for isolation.

# ----------------------------
# Step 1: Sample Class with External Dependency
# ----------------------------

class Data_origin:
    """Simulated Database class."""
    
    def link(self):
        """Simulates a database connection."""
        raise NotImplementedError("This method should link to the database.")

    def retrieve_data(self, query):
        """Simulates fetching data from the database."""
        raise NotImplementedError("This method should retrieve data based on the query.")

class DataHandler:
    """Service that uses the Database class to fetch data."""

    def __init__(self, Data_origin: Data_origin):
        self.Data_origin = Data_origin

    def get_user_data(self, user_id):
        """Fetches user data based on user_id."""
        query = f"SELECT * FROM users WHERE id={user_id}"
        return self.Data_origin.retrieve_data(query)

# ----------------------------
# Step 2: Writing Tests with Mock Objects
# ----------------------------

from unittest.mock import Mock

def test_get_user_data():
    """Test the DataService.get_user_data method using mock objects."""
    
    # Create a mock database object
    mock_Data_origin = Mock(spec=Data_origin)

    # Define the behavior of the fetch_data method
    mock_Data_origin.retrieve_data.return_value = {'id': 5, 'name': 'Zara'}

    # Create an instance of DataService with the mock database
    service = DataHandler(mock_Data_origin)

    # Call the method under test
    result = service.get_user_data(1)

    # Assert the results
    assert result['id'] == 5
    assert result['name'] == 'Zara'
    
    # Verify that the fetch_data method was called with the correct query
    mock_Data_origin.retrieve_data.assert_called_once_with("SELECT * FROM users WHERE id=1")

# To run the tests in this file, use the following command:
# $ pytest example.py