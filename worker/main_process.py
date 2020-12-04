import json


def main_worker(body):
  print(1)
  print(json.loads(body))