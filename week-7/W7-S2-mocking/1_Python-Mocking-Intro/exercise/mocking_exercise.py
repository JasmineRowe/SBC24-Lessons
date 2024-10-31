


import requests

def fetch_data(url):
    """Function to fetch data from an API endpoint."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()


def test_fetch_data():
    """Test the fetch_data function without mocking (not recommended)."""
    url = "https://api.agify.io?name=meelad"
    data = fetch_data(url)

    assert data['count'] == 21
    assert data['age'] == 34 
    assert data['name'] == "meelad" # Check that the fetched data is correct


from unittest.mock import patch

@patch('requests.get')
def test_fetch_data_mocked(mock_get):

    """Test the fetch_data function with mocking."""
    # Arrange: Set up the mock to return a specific response
    mock_get.return_value.json.return_value = {'count': 21, 'age' : 34, 'name' : 'meelad'}
    
    # Act: Call the function under test
    url = "https://api.agify.io?name=meelad"
    data = fetch_data(url)

    
   # Assert: Check the results
    assert data['count'] == 21
    assert data[ 'age'] == 34
    mock_get.assert_called_once_with(url)  # Ensure the mock was called with the correct URL


# To run the tests in this file, use the following command:
# # $ pytest mocking_example.py