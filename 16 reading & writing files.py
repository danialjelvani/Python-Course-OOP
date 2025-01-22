# .\ yani az current location
# ..\ yani yeki boro aghab(albate cd..\ j mide terminal)
# new line tu linux \n vali tu windows \r\n

f = open('file1.txt')
for i in dir(f):
    print(i)
print()
print(f.read())
f.close()

# try finally riske baz mundn file ro km mikone
# rahe behtar:

with open('file1.txt') as f:
    print(f.read())
# agar az indent kharej sham file ro mibnde

f = open('file1.txt')
f2 = f.read()
# ba yek bar read pointer mire akhare file
# va agr dobare read bznim chizi nis bayad ya savesh knim
# ya pointero ba f.seek(0) biarim aval
print(f.read(), '2nd')
print(f.read(), '3rd')
f.seek(1)
print(f.read(), '4th')
print(f2)
f.seek(0)
print(f.read(5), '5th')
# in payini kheili efficiente
for line in f:
    print(line)
f.close()

f = open('file1.txt', mode='w')
f.write('this is line 3\n this is next line')
f.close()
# write krdn pak mikone ghabliaro va overwrite mikone
# append add mikone

f = open('file1.txt', 'a')
f.write('\nappend tu file')
f.close()
f = open('file1.txt', 'r')
print(f.read())
f.close()

# mode r+ ya w+ ham mishe r ham mishe w:
with open('file1.txt', 'r+') as f1, open('file2.txt', 'w+') as f2:
    f1.write('hi danial')
    f2.write('hi again')
    print(f1.read(), '00')
    print(f2.read(), '00')
    # in 2 ta balayio print nakrde chon pointer bade write
    # rfte ta akhar va az hamunja mikhad read kone
    f1.seek(0)
    f2.seek(0)
    print(f1.read(), '11')
    print(f2.read(), '11')

# print ham mitune hamun kare write ro kone:
# f = open('file1.txt', 'w')
# print('danial', file=f)
