'''
    Chatbot pappagallo
'''
from yaml import load, dump
dialoghi = {}
def Inizializzazione () :

  dialoghi['ciao'] = 'ciao, come stai?'
  dialoghi['buongiorno'] = 'buongiorno a te'
  dialoghi['che fai'] = 'stavo dormendo tu?'
  dialoghi['come è sara?'] = 'èbrutta e puzza'
  dialoghi['chi è sara?'] = 'che cosa ti importa'
  dialoghi['oddio stavo per cadere'] = 'abbd che mo cd'
def salva(nome_file):
    global dialoghi
    file = open(f'dialoghi.yaml', 'w', encoding = 'utf-8')
    dati = dump(dialoghi, default_flow_style=False)
    file.write(dati)
    file.close()

def carica(nome_file):
    global dialoghi
    file = open(f'{nome_file}.yaml', 'r', encoding = 'utf-8')
    dati = file.read()
    file.close()
    dialoghi = load(dati)


if __name__=='__main__':
    Inizializzazione()
    carica('dialoghi')
    
    while True:
        domanda = input('domanda ?')
        if domanda == 'fine':
            break
        if domanda in dialoghi:
            risposta = dialoghi[domanda]
            print(risposta)
        else:
            print('questa è una nuova richiesta')
            risposta = input('risposta ?')
            dialoghi[domanda] = risposta
            salva('dialoghi')

print('finito')
      
        
            
       
