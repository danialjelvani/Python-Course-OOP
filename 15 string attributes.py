# merge dictionary ba:
# {**x, **y} or x|y or x.update(y)

# text processing:
# lower case
# remove numbers
# remove punctuations
# remove whitespaces

from string import punctuation
print(punctuation)
print()

mytext = 'Danial & Alireza   ba hm 5 ta (email@yahoo) sakhtan'
print(mytext)
print()


def text_process(text):
    text = text.lower()
    for i in text:
        if i in ''' 0123456789!"#$%&'()*+,-./:;<=>?@[]^_`{|}~\\''':
            # vase inke \ escape sequence nashe bayad 2 ta bezarim \\
            text = text.replace(i, '')
            # delete tu string nadarim vase hamin replace mikonim ba ''

    return text


print(text_process(mytext))
print()

# or rahe dovom:


def text_process2(text):
    text = text.lower()
    text = ''.join(filter(lambda char: not char.isdigit(), text))
    text = ''.join(filter(lambda char: char not in punctuation, text))
    text = ' '.join(text.split())
    # vase monazam krdn text vaghti anvae faseleharo darim az hame bhtr splite

    return text


print(text_process2(mytext))
