import re

text = "The rain in SPAIN stays mainly in the plain"

# Check if the string contains "ain"
check = re.search("ain",text)

# if check:
#     print("Match found")
#     print("Start index: ", check.start())
#     print("End index: ", check.end())
    
#find all occurrences of "ain"

find_all = re.findall("ain",text,re.IGNORECASE)
# print("All occurrences of 'ain': ", find_all)


# Replace all occurrences of a pattern

rep = re.sub("ain","XYZ",text,re.IGNORECASE)
# print("Replaced text: ", rep)

# Character Classes

charClass = re.findall(r"[Sa]tyam",'Satyam good is only good his name is satyam')
print("All occurrences of characters from a to m: ", charClass)