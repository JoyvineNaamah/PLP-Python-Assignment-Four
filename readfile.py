file = open("myData.txt", "r")

print(file.read())

writeDoc = open("myDataFile.txt", "a")
writeDoc.write("This is a write test")