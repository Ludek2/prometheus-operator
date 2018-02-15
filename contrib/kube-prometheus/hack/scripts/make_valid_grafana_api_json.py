#this script takes a json filepath as an argument and prints the json into the standard output
#the script has following functionalities:
# - leads to more consistent results when the json file contains an invisible characters in the end of the file
# - removes id from dashboards that are exported from grafana UI in order to secure compatibility with grafana api
import json
import sys

file_path=sys.argv[1]
data = json.load(open(file_path))
try:
  data['id']= None
except:
  pass
print(json.dumps(data, indent=2, sort_keys=True))
