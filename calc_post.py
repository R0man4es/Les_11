import requests

# addition | difference | division | multiplication
calc_param = {"value_1": 5.6, "value_2": 0, "operation": "division"}
response = requests.post("http://127.0.0.1:8000/calc", json=calc_param)
print(response.text)
