
from yaml import load, dump
dialoghi = {}

dialoghi['ciao'] = 'salve, mi dica'
dialoghi['buongiorno'] = 'che vuoi'
dialoghi['che ore sono'] = 'e io che ne so'
dialoghi['dove è la stazione'] = 'sei troppo piccolo per saperlo'
dialoghi['perchè?'] = 'non sono affari tuoi'
dialoghi['cosa pensi di me?'] = 'perchè dovrei risponderti?'

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

file = open('dialoghi.yaml', 'w', encoding = 'utf-8')
dati = dump(dialoghi, default_flow_style=False)
file.write(dati)
file.close()

print('finito')