import requests

r = requests.post("localhost:8080", data={'a': '1'})
# And done.
print(r.text) # displays the result body.
