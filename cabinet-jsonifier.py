lines = []

json = "["

with open("cabinet-info.txt", "r") as file:
	for line in file:
		if line[-2] != "?":
			json += "{\"id\":\""

			paren = line.find(" (")
			title = line[0:paren]
			containsAndAlternative = False
			if title.find("&") != -1 or title.find("'n") != -1:
				containsAndAlternative = True
			fullyQualifiedTitle = title
			title = "".join(c for c in title if c.isalnum())
			title = title.lower()
			json += (title + "\",\"fullTitle\":\"" + fullyQualifiedTitle + "\",\"isWorking\":")

			if line[-2] == "x":
				json += "false"
			else:
				json += "true"
			json += (",\"searchTerms\":[\"" + title + "\"")

			spaced = line[0:paren]
			spaced = "".join(c for c in spaced if c.isalnum() or c == " ")
			spaced = spaced.lower()
			wordList = spaced.split()
			for word in wordList:
				json += (",\"" + word + "\"")
				# some special cases
				if word.lower() == "ii":
					json += (",\"2\"")
				if word.lower() == "vs":
					json += (",\"versus\"")
			if line[0:paren].lower().find("teenage mutant ninja turtles") != -1:
				json += (",\"tmnt\"")
			if containsAndAlternative:
				json += (",\"and\"")
				json += (",\"&\"")
			

			closeParen = line.find(")")
			if closeParen - paren > 1:
				pub = line[(paren + 2):closeParen]
				pubList = pub.split()
				for p in pubList:
					json += (",\"" + p.lower() + "\"")
			
			json += "]},"

if json[len(json) - 1] == ",":
	json = json[:-1]
json += "]"
with open("games.json", "w") as jsonFile:
	jsonFile.write(json)