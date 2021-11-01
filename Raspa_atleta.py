#Este projeto tem como finalidade criar uma solução que recupere na WEB as informações esportivas de uma pessoa.
# bibliotecas utilizadas
from googlesearch import search
import urllib
import urllib.request
from datetime import datetime

class raspa_url:
        def separa_url(site1,ano,lista_url_sites_palabras_esporte):   #obtem o endereço absoluto do site e o pais
                url_separada=[]
                Informcao_url = {}

                if "//" in site1:
                    pos_barrasd=site1.find("//")+2
                    num_resto_url=len(site1)-pos_barrasd
                    url_separada1 = site1[pos_barrasd:num_resto_url]
                    if "/" in url_separada1:            # separa url do site
                        pos_barrass = url_separada1.find("/")
                        url_separad2 = url_separada1[0:pos_barrass]
# aqui
                Informcao_url3 = [url_separad2]
                Informcao_url3 = Informcao_url3 + [raspa_url.separa_url_generico(resultado, lista_url_sites_palavras_pais, "pais")]
                Informcao_url3 = Informcao_url3 + [raspa_url.separa_url_generico(resultado, lista_url_sites_palavras_cidades, "cidades")]
                Informcao_url3 = Informcao_url3 + [raspa_url.separa_url_generico(resultado, lista_url_sites_palavras_uf, "uf")]
                Informcao_url3 = Informcao_url3 + [raspa_url.separa_url_generico(resultado, lista_url_sites_palavras_tiparq, "tipo arquivo")]
                Informcao_url3 = Informcao_url3 + [raspa_url.separa_url_generico(resultado, lista_url_sites_palabras_correlacionadas,"correlacionados")]
                Informcao_url3 = Informcao_url3 + [raspa_url.separa_url_generico(resultado, lista_url_sites_palabras_esporte, "esporte")]
                Informcao_url3 = Informcao_url3 + [raspa_url.separa_url_generico(resultado, lista_url_sites_palavras_ano, "ano")]
                Informcao_url_lista2.append(Informcao_url3)

        def separa_url_generico(site1, lista,tipo):
            V_return = "NA"
#            print(f" {tipo} ",end="")
            for n in range(0, len(lista)):  # procura esporte na url
                v_achado = str(lista[n]).upper() in site1.upper()
                if v_achado == True:
                    achado = lista[n].upper()
                    V_return=achado
                    break
            return V_return
            #print(f"Func achado {tipo}- > {achado}")
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
print(f"Consultando o nome {nome}")
ano=1942
cont=0
contotal=0
listacerta= []
listaerro=[]
url_separada=[]
#Informcao_url3=[]
Informcao_url_lista=[]
Informcao_url_lista2=[]
lista_url_sites_palavras_pais=["BR"]
lista_url_sites_palavras_cidades = ["PraiaGrande","Santos","SãoPaulo","\RIO","Riojaneiro","Riodejaneiro"]
lista_url_sites_palavras_uf = ["\SP","_sp","_rj","\RJ"]
lista_url_sites_palavras_tiparq=["/imagem/","/doc/"]
ano_corrente1 = datetime.now()
ano_corrente = ano_corrente1.year
lista_url_sites_palavras_ano=[]
lista_ano=[]
while True:             #MONTA A LISTA DE ANOS
      lista_ano = lista_ano+[str(ano)]
      if ano == ano_corrente:
            lista_url_sites_palavras_ano.append(lista_ano)
            break
      ano+=1

lista_url_sites_palabras_correlacionadas = ["resultados", "resultado"
    , "esporte" , "esportes"
    , "esportiva" , "esportivas"
    , "etapa", "etapas"
    , "atletas", "atleta"
    , "premiação", "premiações"
    , "endurance"]

lista_url_sites_palabras_esporte = ["corrida", "natação"
    , "bike", "ciclismo", "maratona", "triathlon"
    , "biatlhon", "duatlhom", "runner", "meia", "marathon"
    ,"basquete", "AQUATHLON","futebol","Ironman", "swimming"]

lista_url_sites_palabras_ok = lista_url_sites_palabras_correlacionadas+lista_url_sites_palabras_esporte
for resultado in search('"'+nome+'"',
                        tld = 'com', lang = 'en',num = 10,
                        start = 0, stop = None, pause = 2.0):
    if valida_site.tipo(resultado): 
        print("\n"+resultado)
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
print("<<< URL >>>")
print("#"*40)

for n in range(0,len(listacerta)):
    print(f" {n+1} - {listacerta[n]}")
    print(f"{Informcao_url_lista2[n]}")
print("#"*40)
"""
                ano_corrente1=datetime.now()
                ano_corrente = ano_corrente1.year

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

"""

"""
lista_url_sites_palavras_ano=["1964","1965","1966","1967","1968","1969"
                                 ,"1970","1971","1972","1973","1974","1975","1976","1977","1978","1979"
                                 ,"1981","1982","1983","1984","1985","1986","1987","1988","1989"
                                ,"1990","1991","1992","1993","1994","1995","1996","1997","1998","1999"
                                , "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010"
                                , "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"
                                , "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030" ]
"""