"""
    Analizzatore di frase
"""

articoli = 'il la lo i gli le un uno una'
s_art = set(articoli.split())
particelle = 'se per in con su tra fra di che a'
s_part = set(particelle.split())

frase = input('scrivi una frase: ')
s_parole = set(frase.split())

print('Parole significative:')
risultato = s_parole - s_art - s_part
print(risultato)

