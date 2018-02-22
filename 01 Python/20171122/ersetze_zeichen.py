def ersetze(text, zeichenAlt, zeichenNeu):
    textNeu = ''
    for z in text:
        if z == zeichenAlt:
            textNeu = textNeu + zeichenNeu
        else:
            textNeu = textNeu + z
    return textNeu

def ersetzeVokale(text, zeichenNeu):
    textNeu = text
    for vokal in ['a', 'e', 'i', 'o', 'u']:
        textNeu = ersetze(textNeu, vokal, zeichenNeu)
    return textNeu

eintext = """
    Drei Chinesen mit dem Kontrabass
    sassen auf der Strasse und erzaehlten sich was.
    Da kam die Polizei, fragt ‚Was ist denn das?‘
    Drei Chinesen mit dem Kontrabass.
    """
