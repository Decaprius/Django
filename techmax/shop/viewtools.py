import json
from . models import *

def gastCookie(request):
    try:
        warenkorb = json.loads(request.COOKIES['warenkorb'])
    except:
        warenkorb = {}

    artikels = []
    bestellung = {'get_gesamtpreis':0, 'get_gesamtmenge':0}
    menge = bestellung['get_gesamtmenge']

    for i in warenkorb:
        menge += warenkorb[i]["menge"]
        artikel = Artikel.objects.get(id=i)
        gesamtpreis = (artikel.preis * warenkorb[i]['menge'])
        bestellung['get_gesamtpreis'] += gesamtpreis
        bestellung['get_gesamtmenge'] += warenkorb[i]['menge']

        artikel = {
            'artikel':{
                'id':artikel.id,
                'name':artikel.name,
                'preis':artikel.preis,
                'bild':artikel.bild
            },
            'menge':warenkorb[i]['menge'],
            'get_summe':gesamtpreis
        }
        artikels.append(artikel)

    return{'artikels':artikels, 'bestellung':bestellung}