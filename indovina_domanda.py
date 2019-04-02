"""
    Ricerca della domanda più inerente alla domanda dell'utente
    Cerca di indovinare tramite un algoritmo di calcolo dall'insieme
    delle parole sgnificative
"""

from yaml import load

dialoghi = {}

articoli = 'il la lo i gli le un uno una'
s_art = set(articoli.split())
particelle = 'se per in con su tra fra di che a'
s_part = set(particelle.split())
altre = 'da si vi questo questa questi queste quello quella quelle che cosa v s'
s_altre = set(altre.split())

def estrai_significative(frase):
    # estrae le parole significative dalla frase
    global s_art, s_part, s_altre
    frase_min = frase.lower()  # abbassa tutte le maiuscole nella frase
    frase_pulita = frase_min.replace('.', ' ').replace(',',' ')
    s_parole = set(frase_pulita.split())
    # print('frase_pulita', frase_pulita, s_parole)
    parole_significative = s_parole - s_art - s_part - s_altre
    return parole_significative
        
def calcola_parole(frase):
    # calcola il numero delle parole significative della frase
    parole_significative = estrai_significative(frase)
    return len(parole_significative)

def confronta_significative(insieme_sig1, insieme_sig2):
    # restituisce l'insieme intersezione tra i due insiemi dati
    # risultato <--- insieme_sig1 intersezione insieme_sig2
    return insieme_sig1.intersection(insieme_sig2)

    
def carica(nome_file):
    # carica i dati dei dialoghi dal file YAML
    global dialoghi
    file = open(f'{nome_file}.yaml','r', encoding = 'utf-8')
    dati = file.read()
    file.close()
    dialoghi = load(dati)

if __name__ == '__main__':
    frase_utente = input('domanda ? ')
    parole_utente = estrai_significative(frase_utente)
    print('parole utente:', parole_utente)
    carica('dialoghi')
    # resinserire il while del loop dell'interazione con l'utente
    # che si chiudeva con 'fine'
    for domanda in dialoghi:
        parole_domanda = estrai_significative(domanda)
        # stampare solo le parole domanda che hanno interseazione non nulla
        # con le parole utente
        parole_comuni = confronta_significative(parole_domanda, parole_utente)
        if  parole_comuni != set():
            print(parole_comuni)
            risposta = dialoghi[domanda]
            print(risposta)
        else:
            # deve imparare la nuova domanda e chiedere la giusta risposta
    # alla fine deve risalvare i dialoghi sul disco
         
