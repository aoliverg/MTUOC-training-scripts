import sys
import codecs
import unicodedata

def is_valid(token):
    valid=True
    if len(token)>50:
        valid=False
        return valid
    for t in token:
        if not unicodedata.category(t)[0]!="C":
            valid=False
            break
    return valid

fentrada=sys.argv[1]

entrada=codecs.open(fentrada,"r",encoding="utf-8")


cont=0
resultat=[]
for linia in entrada:
    linia=linia.rstrip()
    camps=linia.split(": ")
    subword=camps[0]
    if is_valid(subword):
        cadena=str(subword)+": "+str(cont)
        resultat.append(cadena)
        cont+=1

entrada.close()        
sortida=codecs.open(fentrada,"w",encoding="utf-8")
for r in resultat:
    sortida.write(r+"\n")
    
sortida.close()
