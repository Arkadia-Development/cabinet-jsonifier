lines = []

json = "["

with open("cabinet-info.txt", "r") as file:
	for line in file:
		json += "{\"id\":\""

		paren = line.find("(")
		title = line[0:paren]
		title = "".join(c for c in title if c.isalnum())
		title = title.lower()
		json += (title + "\",\"isWorking\":")

		if line[len(line) - 1] == "x":
			json += "false"
		else:
			json += "true"
		json += (",\"searchTerms\":[\"" + title + "\"")

		closeParen = line.find(")")
		if closeParen - paren > 1:
			pub = line[(paren + 1):closeParen]
			pubList = pub.split()
			for p in pubList:
				json += (",\"" + p.lower() + "\"")
		
		json += "]},"

if json[len(json) - 1] == ",":
	json = json[:-1]
json += "]"
with open("games.json", "w") as jsonFile:
	jsonFile.write(json)