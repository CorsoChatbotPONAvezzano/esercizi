'''
    Chatbot pappagallo
'''

def inizializzazione():
    global dialoghi
    dialoghi['ciao'] = 'ciao, come stai?'
    dialoghi['buongiorno'] = 'buongiorno a te'

def salva(nome_file):
    global dialoghi
    file = open(f'{nome_file}.yaml', 'r', encoding = 'utf-8')
    dati = file.read()
    file.close
   dialoghi = load(dati)

    if__name__=='__main__':
        inzializzazione()
        carica('dialoghi')
while True:
    domanda = input('domanda ?')
    if domanda == 'fine':
        break
    if risposta in dialoghi:
        risposta = dialoghi[domanda]
    print(risposta)
    else:
        print('questa è una nuova domanda')
        risposta = input('risposta ?')
        dialoghi[domanda] = risposta
        salva('dialoghi')
    
print('finito')
