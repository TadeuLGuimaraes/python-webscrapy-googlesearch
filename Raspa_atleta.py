#Este projeto tem como finalidade criar uma solução que recupere na WEB as informações esportivas de uma pessoa.
"""
#FASE 1 - Procurando na web - Utilizando a bibliotea googlesearch
            #FASE 1.1
              Filtros das pesquisas atraves do nome e cpfj
              Validar os sites que o link não estão mais funcionando
              Obter atraves da url:
                    Os sites correlacionadosos tipos(esportes, buscadores de informações, juridicos, redes sociais, etc.)
                    Pais
                    Ano.
                    Sites dos organizadores das provas
            #FASE 1.2
              Ler o HTML dos sites e extraindo as informações: inscrições, resultados de provas e etc.
              Resultados, categoria, tempos, local das provas e etc.
              Confirmar as informações obtidas da fase 1.1 (
                Os sites correlacionadosos tipos(esportes, buscadores de informações, juridicos, redes sociais, etc.)
                    Pais
                    Ano.
"""
# bibliotecas utilizadas
from googlesearch import search
import urllib
import urllib.request
from datetime import datetime

class raspa_url:
        def separa_url(site1,ano,lista_url_sites_palabras_esporte):   #obtem o endereço absoluto do site e o pais
                url_separada=[]
                Informcao_url = {}
                ano_corrente1=datetime.now()
                ano_corrente = ano_corrente1.year

                if "//" in site1:
                    pos_barrasd=site1.find("//")+2
                    num_resto_url=len(site1)-pos_barrasd
                    url_separada1 = site1[pos_barrasd:num_resto_url]
                    if "/" in url_separada1:            # separa url do site
                        pos_barrass = url_separada1.find("/")
                        url_separad2 = url_separada1[0:pos_barrass]
                        if ".com." in url_separad2:      #separa do site o pais
                            pos_pais = url_separad2.find(".com.")+5
                            url_pais = url_separad2[pos_pais:pos_barrass]
                        else:
                            url_pais="NA"
                        while True:             #preocura ano na url
                                    if str(ano) in site1:
                                        ano_achado=str(ano)
                                        break
                                    ano+=1
                                    if ano == ano_corrente:
                                        ano_achado="NA"
                                        break
                        v_ret =False
                        for n in range(0, len(lista_url_sites_palabras_esporte)): # procura esporte na url
                            v_esporte = lista_url_sites_palabras_esporte[n].upper() in site1.upper()
                            if v_esporte == True:
                                esporte=lista_url_sites_palabras_esporte[n].upper()
                                break
                            else:
                                esporte ="NA"

                Informcao_url = [url_separad2, url_pais, ano_achado,esporte]
                Informcao_url_lista.append(Informcao_url)           # incl dicionario na lista

class valida_site:
        def tipo(site1):
            """
            :objetivo: validar o tipo de site e correlacionados ao esprotes.
            :param site1: url para avaliação de palavras ou site não correlacionados
            :return: False se o site não correlacionado
            """
            V_ret=False
            V_site=site1.upper()
            for n in range(0,len(lista_url_sites_palabras_ok)):
                    if lista_url_sites_palabras_ok[n].upper() in V_site:
                        V_ret=True
            return V_ret

        def existe(site1):
                try:
                           site = urllib.request.urlopen(site1)
                except Exception as erro:
                        print(f"\033[31m    ERRO: Site não OK..  \033[m:")
                        print(f"\033[32m        erro.__module__            - >\033[m {erro.__module__}")
                        print(f"\033[32m        erro.__class__             - >\033[m {erro.__class__} ")
                        print(f"\033[32m        erro.__repr__()            - >\033[m {erro.__repr__()}")
                        print(f"\033[32m        erro.__str__()             - >\033[m {erro.__str__()} ")
                        print(f"\033[32m        erro.__suppress_context__  - >\033[m {erro.__suppress_context__}")
                        print(f"\033[32m        erro.__traceback__         - >\033[m {erro.__traceback__}")
                        print(f"\033[32m        erro.args                  - >\033[m {erro.args}")
                        print(f"\033[32m        erro.__cause__             - >\033[m {erro.__cause__}")
                        print(f"\033[32m        erro.__context__           - >\033[m {erro.__context__}")
                        print(f"\033[32m        erro.__doc__               - >\033[m {erro.__doc__}")
                        listaerro.append(resultado)
                else:
                        print(f"Site OK")
                        #print(site.read())
                        #breakpoint()
# trata os dados
# mostra os dados
nome=str(input("Digite um nome completo - > ")).upper().strip()
ano=1999
teste=0
cont=0
contotal=0
listacerta= []
listaerro=[]
url_separada=[]
Informcao_url_lista=[]

lista_url_sites_palabras_ok = ["resultados", "corrida", "natação"
    , "bike", "ciclismo", "maratona", "triathlon"
    , "biatlhon", "duatlhom", "runner"
    , "esporte", "meia", "esportiva", "marathon"
    , "etapa", "atletas", "atleta", "basquete"
    , "premiação", "AQUATHLON","futebol"]

lista_url_sites_palabras_esporte = ["corrida", "natação"
    , "bike", "ciclismo", "maratona", "triathlon"
    , "biatlhon", "duatlhom", "runner", "meia", "marathon"
    ,"basquete", "premiação", "AQUATHLON","futebol"]

for resultado in search('"'+nome+'"',
                        tld = 'com', lang = 'en',num = 10,
                        start = 0, stop = None, pause = 2.0):
    if valida_site.tipo(resultado): 
        print(resultado)
        valida_site.existe(resultado) 
        print("*" * 40)
        listacerta.append(resultado)
        raspa_url.separa_url(resultado,ano,lista_url_sites_palabras_esporte)
        cont += 1
    contotal+=1
print("#"*40)
print(f"Qtd de sites correlacionados                     -> {cont}")
print(f"Qtd de sites não correlacioandos                 -> {contotal}")
print("                                                 ---------")
print(f"                                                    {contotal+cont}")
print("-"*40)
print(f"Qtd de sites correlacioandos com \033[31merro de acesso \033[m -> {len(listaerro)}")
print(f"Qtd de sites correlacioandos com \033[32macesso ok      \033[m -> {cont-len(listaerro)}")

print("#"*40)
for n in range(0,len(listacerta)):
    print(f" {n+1} - {listacerta[n]}")
print("#"*40)
for n1 in range(0,len(url_separada)):
    print(f" {n1 + 1} - {url_separada[n1]}")
for n1 in range(0,len(Informcao_url_lista)):
    print(f" {n1 + 1} - {Informcao_url_lista[n1]}")
