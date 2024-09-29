import requests
from calculator_client.client import Client
from calculator_client.api.actions import calculate
from calculator_client.models.calculation import Calculation
from calculator_client.models import ResultResponse
from calculator_client.models.opertions import Opertions


class TestCalcApi ():
    def test_clculate(self):

        url = 'http://localhost:5000/calculate'
        payload = {
            "operation": "add",
            "operand1": 1,
            "operand2": 2
        }
        # s
        response = requests.post(url, json=payload)

        assert response.status_code == 200

        data = response.json()
        assert isinstance(response.json(), dict)
        assert 'result' in data
        assert data['result'] == 3

    def test_auto_code(self):
        client = Client("http://localhost:5000/")
        calculation = Calculation(
            operation=Opertions.ADD, operand1=1, operand2=1)
        response: ResultResponse = calculate.sync(
            client=client, body=calculation)
        assert response.result == 2


'''# Inspect the sync function signature
print(calculate.sync.__doc__)


# Initialize the client with the base URL of the API
client = Client(base_url="http://localhost:5000")

# Create a Calculation object with the desired operation and operands
calculation = Calculation(
    operation=Opertions.ADD,  # Or any operation like Operations.SUBTRACT
    operand1=5,
    operand2=3
)

# Perform the calculation
# response: ResultResponse = calculate.sync(client=client, json_body=calculation)

response: ResultResponse = calculate.sync(client=client, body=calculation)


# Print the result
if response:
    print(f"Result: {response.result}")
else:
    print("Failed to get a response from the API")
'''


'''
'''
