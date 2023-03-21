from django import template


register = template.Library()

RUDE_WORDS = [
    'space',
    'covid-19',
    'year',
    'world',
]


@register.filter()
def censor(text):
    for word in text.split():
        if word.lower() in RUDE_WORDS:
            text = text.replace(word, f"{word[0]}{'*'*(len(word)-1)}")
    return text

