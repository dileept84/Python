#Take list as user input and print all names whi have grater than 5 letters

lst = []                            #Empty list
n= int(input("enter list"))        # Taking user input
for i in range(n):
    name = str(input())           #Again user input for string type
    lst.append(name)              #Appending input string to list
print(lst)
j=0
for j in range(0, len(lst)):
    if len(lst[j])>5:
        print(lst[j])
    j+=1
