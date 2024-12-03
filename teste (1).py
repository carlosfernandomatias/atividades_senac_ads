import requests 


url = "https://x8ki-letl-twmt.n7.xano.io/api:-Fpz9RKE/teste"

headers=  {
"Authorization" : "Bearer eyJhbGciOiJBMjU2S1ciLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiemlwIjoiREVGIn0.dSAP8pZK5agdOI2qAK-CGQ3r3mj2T22JKT7CzwUFYdIQTswMB5HE7R1x4RMluXK9DRJ2ZP4MJhSD3fKfuHJqIHvAa7KWZS8-.ciUFBNoo3CbsQwSZNSFtqA.hl7Rp_3ZBtQAfmN8A72VgzsEyYTlOh21dlsx4O7mLgnnHu25k2Oy6FV4DFajWIuQzs9P5WbXp2ziG4X3-C9Z-tnv3FCHj1mBNVESxUTHptmCw7lldOBu0uf_5dfI_JpHlSRNDqVnE4DV3souIxeus2hSNcLJ6jm7u4--jgvSYIQ.kmp0U3icZe3GWmclSR0pzu0TJvE1RaouSCQj7oQUGk0"
}

payload = {
  "nome": "carlos",
  "cpf": "ddddddd"
}
response = requests.post(url, json = payload, headers=headers)

print(response.text)