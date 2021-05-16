import requests

f = open("config.txt", "r")
URL = f.read()

def test(df):
  df = df.to_json()
  r = requests.post(url=URL+"save_data", json=df)
  return r
