import string

lines = []

json = "["

with open("cabinet-info.txt", "r") as file:
	for line in file:
		if line != file[0]:
			json += ","
		json += "{\"id\":\""

		paren = line.find("(")
		title = line[0:paren]
		title = filter(title.isalnum, string.printable).lower()
		json += (title + "\",\"isWorking\":")

		if line[len(line) - 1] == "x":
			json += "false"
		else:
			json += "true"
		json += (",\"searchTerms\":[\"" + title + "\"")

		closeParen = line.find(")")
		if closeParen - paren > 1:
			pub = line[paren:(closeParen + 1)]
			pubList = pub.split()
			for p in pubList:
				json += (",\"" + p + "\"")
		
		json += "]}"

json += "]"
with open("games.json", "w") as jsonFile:
	jsonFile.write(json)