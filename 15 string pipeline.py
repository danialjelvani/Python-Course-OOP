# ye string pipeline koli:

from string import punctuation
from abc import ABC, abstractmethod


class TextProcessor(ABC):
    @abstractmethod
    def transform(self, text):
        pass

    # transformer 1:


class ConvertCase(TextProcessor):
    def __init__(self, casing='lower'):
        self.casing = casing

    def transform(self, text):
        if self.casing == 'lower':
            return text.lower()
        elif self.casing == 'upper':
            return text.upper()
        elif self.casing == 'title':
            return text.title()


# transformer 2:

class RemoveDigit(TextProcessor):
    def transform(self, text):
        text = ''.join(filter(lambda char: not char.isdigit(), text))
        return text


# transformer 3:

class RemoveSpace(TextProcessor):
    def transform(self, text):
        return ' '.join(text.split())


# transformer 4:

class RemovePunkt(TextProcessor):
    def __init__(self, replace_char=' '):
        self.replace_char = replace_char

    def transform(self, text):
        return ''.join(char if char not in punctuation else self.replace_char for char in text)


# pipeline:

class StringPipeline:
    def __init__(self, *args):
        self.transformers = args

    def transform(self, text):
        for i in self.transformers:
            text = i.transform(text)
        return text

    def __str__(self):
        return '''Transforms text with transformers:
        ConvertCase(lower,upper,title) RemoveDigit RemovePunkt RemoveSpace'''


t1 = StringPipeline(
    ConvertCase('upper'),
    RemoveDigit(),
    RemovePunkt(replace_char='-'),
    RemoveSpace()
)
mytext = 'Danial &   Mahsa are @ the beach club 2'
print(mytext)
print()
print(t1.transform(mytext))
