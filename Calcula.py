#!C:\Program Files (x86)\Ampps\python\python.exe 

import cgi
args= cgi.FieldStorage()
valor1=int(args['numero1'].value)
valor2=int(args['numero2'].value)
suma=valor1+valor2

print ("Content-type: text/plain\n\n")
print ("La suma es  ",suma)