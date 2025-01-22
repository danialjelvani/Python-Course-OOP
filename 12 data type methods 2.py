# list methods:

lii = [
    'danial',
    'mahsa',
    '2',
    33,
]

lii.extend(lii)
print(lii)
print()
# extend o += hardo ye kar miknn
lii += lii
print(lii)
lii = [
    'danial',
    'mahsa',
    '2',
    33,
]
print()
lii.insert(1, 'bashe pas')
print(lii)
print()
lii.pop(2)
print(lii)
print()

# dic methods:

dic = {
    'danial': 10,
    'mahsa': 30,
}
# agar dic['ali'] benevisim error mide chon tu
# list nis vase hamin mitunim az get estefade knim
# va bgim chi age nabud return kn
print(dic.get('ali'))
print(dic.get('ali', 0))
# rahe asoone plus dic ha:
# dic += dic plus ro tu dic nadarim injuri
# tuple plus dare ama dic nadare:
print({**dic, **dic})
dic2 = {'alireza': 40}
print({**dic, **dic2})
print()

# set methods:

s1 = {1, 2, 3}
s2 = {1, 4, 5, 6}
print(s1.union(s2))  # s1|s2 albate ba union in tafavoto
# dare k tu union har chize iterabel mese listo string mitune add she
# vali tu s1|s2 faght bayad hardo set bashan
print(s1.intersection(s2))  # s1&s2
print(s1.difference(s2))  # s1-s2
# poshte ham ham mitunn bian
print(s1.union(s2).difference(s1).intersection(s2))

# symmetric_difference mishe ejtema-eshterak ba alamate ^
print(s1.symmetric_difference(s2))

# .issubset() yani zir majmooe hast? ba alamate <
# .issuperset() yani un zir majmooe in hast? ba alamate >

# farghe union() ba union_update() ine k tu union_update() khode s1 ro
# ham taghir mideo update mikone

# s1.remove() va s1.discard() hazf mioknn ba in tafavot
# k age peidash nkrd tu remove error mide tu discard na
