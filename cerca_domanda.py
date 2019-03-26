"""
    Ricerca della domanda più inerente alla domanda dell'utente
"""

from yaml import load

dialoghi = {}

articoli = 'il la lo i gli le un uno una'
s_art = set(articoli.split())
particelle = 'se per in con su tra fra di che a'
s_part = set(particelle.split())
altre = 'si vi questo questa questi queste quello quella quelle che cosa v s'
s_altre = set(altre.split())

def calcola_parole(frase):
    # calcola il numero delle parole significative della frase
    global s_art, s_part, s_altre
    frase_min = frase.lower()  # abbassa tutte le maiuscole nella frase
    frase_pulita = frase_min.replace('.', ' ').replace(',',' ')
    s_parole = set(frase_pulita.split())
    # print('frase_pulita', frase_pulita, s_parole)
    parole_significative = s_parole - s_art - s_part - s_altre
    return len(parole_significative)

def carica(nome_file):
    # carica i dati dei dialoghi dal file YAML
    global dialoghi
    file = open(f'{nome_file}.yaml','r', encoding = 'utf-8')
    dati = file.read()
    file.close()
    dialoghi = load(dati)

if __name__ == '__main__':
    frase_utente = input('domanda ? ')
    n_parole_utente = calcola_parole(frase_utente)
    print(n_parole_utente)
    carica('dialoghi')
    for domanda in dialoghi:
        risposta = dialoghi[domanda]
        n = calcola_parole(domanda)
        if n == n_parole_utente:
            print('domanda: ', domanda, n)
        #print('risposta: ', risposta)
        

    
