from sys import argv #set some valuables here
script,filename = argv
txt = open(filename)

print(f"Here's your file {filename}:") #print the sentence ,which contains file 
print(txt.read()) # open the file 

file_again = input("enter your file name again")

txt_again = open(file_again)
print(txt_again.read())
