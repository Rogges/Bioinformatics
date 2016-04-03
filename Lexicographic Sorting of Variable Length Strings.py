list1=['C','B','T', 'G', 'F', 'X', 'N','I', 'Y', 'A', 'P', 'S']
newlist=[]

#list1 contains letters in the exact lexicographical order you want
#newlist will contain the ordered permutations of list1

for letter in list1:
  list2=[letter]
  newlist.append(list2)
  for letter2 in list1:
    y=[[letter,letter2]]
    newlist.append(y)
    z=[[letter,letter2,letter3] for letter3 in list1]
    newlist.append(z)

#the for loops generate strings of length 1-3 in correct lexicographic order
#to increase the maximum length, more loops need to be added with more list comprehensions

for list in newlist:
  for letters in list:
    print(''.join(letters))
