'''
    Chatbot pappagallo
'''

dialoghi = {}

dialoghi['ciao'] = 'ciao, come stai?'
dialoghi['buongiorno'] = 'buongiorno a te'

dialoghi['buonasera'] = 'buonasera, a te e famiglia'
dialoghi['buon pomeriggio'] = 'buon pomeriggio, a te e famiglia'

while True:
    domanda = input('domanda ?')
    if domanda == 'fine':
        break
    risposta = dialoghi [domanda]
    print(risposta)
    else:
        print('questa è una nuova domanda')
        risposta = input('risposta ?')
        dialoghi[domanda] = risposta
        
    
file = open('dialoghi.yaml', 'w' encoding='utf-8'
dati = dump(dialoghi, default_flow_style=False)
file.write(dati)
file.close()


print('finito')
