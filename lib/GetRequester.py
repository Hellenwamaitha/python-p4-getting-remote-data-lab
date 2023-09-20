import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404)
            return response.text  # Return the response body as text
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None  # Return None in case of an error

    def load_json(self):
        response_body = self.get_response_body()  # Fetch the response body
        if response_body is not None:
            try:
                data = json.loads(response_body)  # Parse the response body as JSON
                return data
            except json.JSONDecodeError as e:
                print(f"JSON Decode Error: {e}")
                return None  # Return None in case of JSON decoding error

# Example usage:
if __name__ == "__main__":
    # Initialize the GetRequester with a URL
    url = " https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    requester = GetRequester(url)

    # Get and print the response body
    response_body = requester.get_response_body()
    print("Response Body:")
    print(response_body)

    # Load JSON data from the response body and print it
    json_data = requester.load_json()
    if json_data:
        print("\nJSON Data:")
        print(json_data)
