import json

f = open("data/data_influencer.json");

data = json.load(f)

f.close()

for i in data:
	print(i["Username"][1:])

