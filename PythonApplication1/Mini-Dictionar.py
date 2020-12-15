import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def cautare_cuvant(cuvant):
     cuvant = cuvant.lower()
     
     if cuvant in data:  
      if type(data[cuvant]) == list:
          for item in data[cuvant]:
              print(item)
        
     else:
        if len(get_close_matches(cuvant.lower(),data.keys(),3,0.8))>0:
             cuvConf=get_close_matches(cuvant.lower(),data.keys())[0]
             yes = input("Ai vrut sa scrii: '%s' ?[yes/no] " % cuvConf)
             if(yes == "yes"):
                if type(data[cuvant]) == list:
                    for item in data[cuvant]:
                        print(item)
             elif yes=="no":
                 main()
        else:
             print("Cuvantul nu exista")
           

def main():
    cuvant = input("Cauta un cuvant: ")
    cautare_cuvant(cuvant)
   

main()





 