import re

sample_text = "Singapore is an asian country. Singapore has 4 national languages, namely, tamil, english, ,malay and mandarin"


# 1. Search the string to see if it starts with "Sin" and end " rin"
print ("Search the string to see if it starts with \"Sin\" and ends with \"rin. ")
print (f"Given text: #{sample_text}#")
print (f"Given Text : #{sample_text}#")


searchPattern = "^Sin.*ine.$"
matchObject = re.search(searchPattern, sample_text)

if matchObject:
    print ("Match exists")
    print (matchObject)

else:
    print ("Match not exist")


#2. Find all function 
# finds all matches 
fidnAllResult = re.findall("Singapore", sample_text)
print ("re.findall => {}".format(fidnAllResult))


# 3. Search function
searchResult = re.search("country", sample_text)
print ("re.search(\"country\", sampleText) ===> {}".format(searchResult))

# 4. split function
print ("split at each white space character")
splitResult = re.split("s", sample_text)
print(splitResult)


# 5. sub function. replace every white-space character with the number 9 
subResult = re.sub("\s", "9", sample_text)
print ("re.sub(\"\s\", \"9\", sampleText) => {} ".format(subResult))

subResult  = re.sub("\s", "9", sample_text, 3)
print ("re.sub(\"\s\", \"9\", sampleText, 3) => {} ".format(subResult))



# 6. match object example
matchObject = re.search("Singapore", sample_text)
if matchObject:
    print("matchObject.span() => {}".format(matchObject.span()))
    print ("matchObject.string => {}".format(matchObject.string))
    print ("macthObject.group() => {}".format(matchObject.group()))