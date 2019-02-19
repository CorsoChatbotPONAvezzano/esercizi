'''
    Chatbot pappagallo
'''
from yaml import load, dump
dialoghi = {}
def inizializzazione () :

   dialoghi['ciao'] = 'ciao, come stai?'
   dialoghi['bungiorno'] = 'buongiorno a te'
   dialoghi['come stai'] = 'molto male'
   dialoghi['alice non potra mai essere una programmatrice'] = 'lo so'
   dialoghi['con chi dovrebbe stare alice?'] = 'sono convinto che dovrebbe stare con marco'
   dialoghi['sono convinto di poter scalare l everest'] ='ok'
   dialoghi['intorno a me?'] = 'c e gente che indossa occhiali da soooole ma e notte e il sole non ce sara perche fanno aaafteeer'
def salva(nome_file) :
    global dialoghi
file = open (f'dialoghi.yaml' , 'w' , encoding = 'utf-8')
dati = dump(dialoghi, default_flow_style=False)
file.write(dati)
file.close()

if __name__=='__main__':
    inizializzazione()
    while True:
        domanda = input('domanda?')
        if domanda == 'fine':
           break
        if domanda in  dialoghi:
           risposta = dialoghi[domanda]
           print(risposta)
        else:
            print('questa è unanuova richiesta')
            risposta= input('risposta?')
            dialoghi[domanda] = risposta
            salva('dialoghi')
    print('finito')        
    

   
          
    

