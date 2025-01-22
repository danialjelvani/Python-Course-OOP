# string methods:

email = 'mdkfmsatgmail.com'
# find az index 3 ta 10 age nabud -1 mide
if email.find('@', 3, 10) == -1:
    print('invalid email')
print(email.index('m'))
print(email.find('m'))
print(email.rfind('c'))
# har do mign tu index 0 m darim vali index age nadashtim
# value error mide find -1 mide
# rfind az samte rast migrde
# rindex ham hamintore
print(email.replace('at', '@'))
# library re pishrafte findo replace ina dare
s = '69415'
print(s.isdigit())
a = '   nnfrnl  nk n k  '
# space avalo akharo hazf mikone
print(a.strip())
# rstrip o lstrip hm darim
print(s.center(12, '-'))
# .center miare vasat .ljust miare chap
print(s.ljust(10))
print(s.rjust(10))
print(s.zfill(10))
names = ['ali', 'danial', 'mahsa']
print('**'.join(names))
b = 'www.google.com'
print(b.rsplit(sep='.', maxsplit=1))
