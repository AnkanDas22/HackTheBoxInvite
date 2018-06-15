import base64
import requests

code=base64.b64decode((requests.post("https://www.hackthebox.eu/api/invite/generate").text)[29:].split('"')[0])
print(code)

