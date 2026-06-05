###reading a file
file=open("11-File Handling/test.txt","r") #open file
content=file.read() #read file
file.close() #close file VERY IMPORTANT
print(repr(content)) #repr() is used the get the raw string representation
items=content.split("\n") #split the content by new line and store it to a list
items.sort() #sort the list alphabetically
for item in items:
    print("- " + item)