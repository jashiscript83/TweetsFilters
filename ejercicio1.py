import json

tweets= []


def get_values():
    sentimientos = open("Sentimientos.txt")
    valores = {}
    for linea in sentimientos:
        (termino,valor) = linea.split("\t")
        valores[termino] = int(valor)
    return valores

archivo_valores = get_values()


def get_tweets():


    file = open("salida_tweets.txt")

    for linea in file:
        all_tweets= json.loads(linea)
        if 'text' in all_tweets.keys():
            tweets.append(all_tweets['text'].split(" "))
  
    return tweets



lista_tweets = get_tweets()


for n in lista_tweets:
    suma = 0
    
    lineaTweet= " ".join(map(str, n))
    
    for item in n:

        

        if str(item.lower()) in archivo_valores.keys():
    
            suma = suma + archivo_valores[str(item).lower()]
          

    print('El tweet --> ', lineaTweet, 'tiene un valor asociado de: ', suma)
