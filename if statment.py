Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> b=20
>>> if(a==10):
	print(a)
	if(b==20):
		print(b)
		print("the statement is true")

		
10
20
the statement is true
>>> a=10
>>> b=20
>>> if(a==10):
	print(a)
	if(b==24):
		print(b)
		print("the statement is true")
		
SyntaxError: multiple statements found while compiling a single statement
>>> if(a==10):
	print(a)
	if(b==24):
		print(b)
		print("the statement is true")

		
10
>>> 
