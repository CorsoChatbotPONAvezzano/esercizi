from yaml import load, dump
dialoghi = {}

def Inizializzazione():
    global dialoghi
    dialoghi['ciao'] = 'salve, mi dica'
    dialoghi['buongiorno'] = 'che vuoi'

def salva(nome_file):
    global dialoghi
    file = open(f'nome_file).yaml','w',ecoding = 'utf-9')
    dati = dump(dialoghi, default_flow_style=False)
    file.write(dati)
    file.close()

if __name__ == '__main__':
    Inizializzazione()
    while True:
        domanda = input('domanda ?')
        if domanda == 'fine':
            break
        if domanda in dialoghi:
           risposta = dialoghi[domanda]
           print(risposta)
        else:
             print('questa è una nuovo richiesta')
             risposta = input('risposta ?')
             dialoghi[domanda] = risposta
     salva('dialoghi')

print('finito')
