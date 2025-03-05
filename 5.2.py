
import copy 
def mesege(dct,count=3): 
    if count > 0: 
        sub=input("ведите модели:") 
        kan=copy.deepcopy(dct) 
        kan["html"]["body"]["div"]=f'У нас самая низкая цена на {sub}' 
        print(kan) 
        return mesege(dct,count-1) 
site = { 
'html': { 
'head': { 
'title': 'Куплю/продам телефон недорого' 
}, 
'body': { 
'h2': 'У нас самая низкая цена на iPhone', 
'div': 'Купить', 
'p': "Продать" 
} 
} 
} 
mesege(site,int(input("количество сайтов")))