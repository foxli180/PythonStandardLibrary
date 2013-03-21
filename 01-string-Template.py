import string

values = {'var':'foo'}

t = string.Template('''
varible          : $var
Escape           : $$
Variable in text : ${var}iable
NotExist         : $notexist_try_safe_substitute  
''')

print ('TEMPLATE:', t.safe_substitute(values)) #python 3
#print 'TEMPLATE:', t.safe_substitute(values) #python 2.7

###
# to use string format print, you should add s after the variables,
# compare to template,  $var and in string  %(var)s a
# character 's' after the %(var)
# and the %(var)siable the 's' between '%(var)' and 'isable'
###
s = '''
varible          : %(var)s 
Escape           : %%
Variable in text : %(var)siable
'''



print ('INTERPROLATION:', s % values) #python 3
# print 'INTERPROLATION:', s % values #python 2.7
