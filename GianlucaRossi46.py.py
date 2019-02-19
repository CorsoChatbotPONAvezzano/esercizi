
from yaml import load, dump
dialoghi = {}
def inizializzazione():
    global dialoghi
    dialoghi['ciao'] = 'salve, mi dica'
    dialoghi['buongiorno'] = 'che vuoi'
    dialoghi['che ore sono'] = 'e io che ne so'
    dialoghi['dove è la stazione'] = 'sei troppo piccolo per saperlo'
    dialoghi['perchè?'] = 'non sono affari tuoi'
    dialoghi['cosa pensi di me?'] = 'perchè dovrei risponderti?'

def salva(nome_file):
    global dialoghi
    file = open(f'nome_file).yaml','w',ecoding = 'utf-9')
    dati = dump(dialoghi, default_flow_style=False)
    file.write(dati)
    file.close()
    
def carica(nome_file):
    global dialoghi
    file = open(f'(nome_file).yaml','r', encoding = 'utf-8')
    dati = file.read()
    file.close()
    dialoghi = load(dati)
    

if __name__ == '__main__':
    Inizializzazione()ù
    carica ('dialoghi')
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

