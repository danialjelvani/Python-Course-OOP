# extract emails from file

email = 'danialjelvani@gmail.com'
index = email.find('@')
print(email[index+1:])

# or:

print(email.split('@')[1])
