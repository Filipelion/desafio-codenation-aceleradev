from datetime import datetime

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000},

]

hora_certa = lambda h: datetime.fromtimestamp(h)
absolute_time = datetime.now()
inicio_noturno = absolute_time.replace(hour=22, minute=0, second=0, microsecond=0)
fim_noturno = absolute_time.replace(hour=6, minute=0, second=0, microsecond=0)

min_diurno = lambda hora : (hora.time() < inicio_noturno.time()) and (hora.time() > fim_noturno.time())

def classify_by_phone_number(records):
    origem_dic = {}

    for i in records:
        start_call = hora_certa(i["start"])
        end_call = hora_certa(i["end"])
        duration_call = end_call - start_call


        diurno_total = min_diurno(start_call)
        if min_diurno(start_call) == min_diurno(end_call):
            valor = tarifa(diurno_total, (duration_call.seconds)/60)
            dic_add(i["source"], valor, origem_dic)

        else:
            minutos_cobrados = meia_tarifa(start_call, end_call)
            valor = tarifa(True, (minutos_cobrados.seconds)/60)
            dic_add(i["source"], valor, origem_dic)


    lista_final = sorted(origem_dic.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    entrega = []
    for i in lista_final:
        entrega.append({'source': i[0], 'total': i[1]})

    return entrega


def tarifa(horario, minutos_cobrados):
    if horario:
        return 0.36 + (int(minutos_cobrados) * 0.09)
    else:
        return 0.36

def meia_tarifa(inicio, fim):
    if ((min_diurno(inicio)) == True) and ((min_diurno(fim)) == False):
        minuto_cobrado = inicio_noturno - inicio
        return minuto_cobrado

    elif ((min_diurno(inicio)) == False) and ((min_diurno(fim)) == True):
        minuto_cobrado = fim - fim_noturno
        return minuto_cobrado
    else:
        return print("error")

def dic_add(origem, valor, dic):
    if origem not in dic:
        dic[origem] = round(valor, 2)
    else:
        valor_anterior = dic[origem]
        dic[origem] = round(valor_anterior + valor, 2)

classify_by_phone_number(records)
