#!/usr/bin/python

#https://tutorialspoint.com/unix_commands/echo.htm
# Examples 3. -> 6.
# echo -e '...' [SHELL] -> print "..." [PYTHON]
'''
print "Hello World!"
Hello World!
'''
'''
#Example 3
print "Here \bthe \bspaces \bare \bbackspaced."
Herethespacesarebackspaced.
'''
'''
#Example 4
print "Here \nthe \nspaces \nare \nnewlined."
Here 
the 
spaces 
are 
newlined.
'''
'''
#Example 5
print "Here \tthe \tspaces \thave \thorizontal \ttab \tspaces."
Here 	the 	spaces 	have 	horizontal 	tab 	spaces.
'''
'''
#Example 6
print "Here \vthe \vspaces \vhave \vvertical \vtab \vspaces."
Here
     the
         spaces
                have
                     vertical
                              tab
                                  spaces.
'''
'''
#Example 7
print "\t\t\t\t\t\tHere \n\t\t\t\t\tthe \n\t\t\t\tspaces \n\t\t\thave \n\t\tvertical \n\ttab \nspaces."
'''
'''
#Example 8
a = 6
b = 4
print a + b
'''

#Example 9

x=input("Ievadiet X\n")
y=input("Ievadiet Y\n")
print "x =",x, "y =",y, "Summa =", x + y
