q1="""How do you concatenate two strings in Python?
A.str1 . str2
B.str1 + str2
C.str1 , str2
D.concat(str1, str2)"""

q2="""How do you create a dictionary using a comprehension in Python?
A.{key: value for key, value in iterable}
B.dict(iterable)
C.create_dict(iterable)
D.{key, value in iterable}"""

q3="""How do you create a multiline string in Python?
A."This is a multiline string"
B.'This is a multiline string'
C.'''This is a multiline string'''
D.(a and b)"""

q4="""How do you convert a floating-point number to an integer in Python?
A.int(number)
B.float_to_int(number)
C.number.int()
D.convert(int, number)"""

q5="""How do you convert a list of strings to a single string in Python?
A."".join(list)
B.str(list)
C.convert(list, str)
D." ".join(list)"""

q6="""What is the output of the following code?
x=[1, 2, 3, 4]
y=filter(lambda a: a % 2 == 0, x)
print(list(y))
A.[1, 3]
B.[2, 4]
C.[1, 2, 3, 4]
D.[]"""

q7="""How do you find the length of a list in Python?
A.len(list)
B.length(list)
C.list.length()
D.count(list)"""

q8="""What is the output of the following code?
x = "Hello"
print(x[1:4])
A."Hell"
B."ello"
C."ell"
D.Error"""

q9="""What is a variable in Python?
A.A reserved word
B.A data type
C.A location in memory to store data
D.A function"""

q10="""What is the scope of a global variable in Python?
A.Limited to the function it is defined in
B.Limited to the module it is defined in
C.Limited to the class it is defined in
D.Limited to the block it is defined in"""

q11="""name = ['Alex', 'Emma', 'Bob', 'Lucas']
pos = name.index("GeeksforGeeks")
print(pos * 3)
A.0
B.3
C.None
D.ValueError: 'GeeksforGeeks' is not in list"""

q12="""Find the output of the following program: 
li = ['Alex', 'Emma', 'Bob', 'Lucas']
print(li[1][-1])
A.r
B.b
C.s
D.a"""

questions={q1:"B",q2:"A",q3:"C",q4:"A",q5:"D",q6:"B",q7:"A",q8:"C",q9:"C",q10:"B",q11:"D",q12:"D"}

name=input("Enter your name:")
print("Hello",name,"Welcome to the quiz")
score=0
for i,j in questions.items():
	print()
	print(i)
	option=input("Do you want to skip this question(Yes/No):")
	if option=="yes":
		continue
	ans=input("Enter your answer (A/B/C/D):")
	if ans==questions[i]:
		print("Correct answer you got 1 point")
		score=score+1
		print("Correct score is:",score)
	else:
		print("Wrong answer you lost 1 point")
		print("Correct score is:",score)
print("Final score is:",score)


