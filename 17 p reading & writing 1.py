# count words in txt file:

from collections import Counter
with open('file3.txt', 'r') as f:
    text = f.read()
print(len(text.split()))
count = {}
for w in text.split():
    count[w] = count.get(w, 0) + 1
print(count)
print()

# or ba collections va counter:


print(Counter(text.split()))

# agar maximum tekrar ro bekhaim khode
# counter b tartib ziad b kam michine
# ama ba max ham mishe k besh key bedim:
# max key:
print(max(count))
# max value:
print(max(count, key=count.get))
# max longest word:
print(max(count, key=len))
