# decode nazi messages:
# char shifting
# chon ascii 128 chare modesho b 128 migirim
# k age kamtr bishtr shod ok bashe

content1 = 'mikhaim decode knim textio k tush hi danial encode shode va nmidunm shiftesh chand e'

content2 = '-)+(!)-`$%#/$%`+.)-`4%84)/`+`453(`()`$!.)!,`%.#/$%`3(/$%`6!`.-)$5.-`3()&4%3(`#(!.$`%'


def char_shift(text, shift):
    x = 0
    for char in text:
        ord_char = (ord(char) + shift) % 128
        char = chr(ord_char)
        text = text.replace(text[x], char)
        # in kare bala ro ba '' += char hm mishod neveshtesh
        x += 1
    return text


def decoding_system(text):
    for x in range(128):
        if 'hi danial' in char_shift(text, x).lower():
            print(x, '\n')
            print(char_shift(text, x))


decoding_system(content2)
