# write data to the file demo.txt
f=open("demo.txt","w")
f.write("Python is an interpreted high level general purpose programming language.Its design philosophy emphasizes code readability with its use of significant indendation")
f.close()
# read content from demo.txt file
f=open("demo.txt","r")
content=f.read()
print(content)
f.close()
# appending additional text to demo.txt in new line
f=open("demo.txt","a")
f.write("\nIt is the language constructs as well as its object oriented approach aim to help programmer write clear,logical code for small and large scale.")
f.close()

