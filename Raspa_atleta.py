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

                if "//" in site1: # separa url do site
                    pos_barrasd=site1.find("//")+2
                    num_resto_url=len(site1)-pos_barrasd
                    url_separada1 = site1[pos_barrasd:num_resto_url]
                    if "/" in url_separada1:
                        pos_barrass = url_separada1.find("/")
                        url_separad2 = url_separada1[0:pos_barrass]
                Informcao_url3 = [url_separad2]
                # inicia raspagem da url
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
            for n in range(0, len(lista)):
                v_achado = str(lista[n]).upper() in site1.upper()
                if v_achado == True:
                    achado = lista[n].upper()
                    V_return=achado
                    break
            return V_return

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
Informcao_url_lista=[]
Informcao_url_lista2=[]
ano_corrente1 = datetime.now()
ano_corrente = ano_corrente1.year
lista_url_sites_palavras_ano=[]
lista_ano=[]
#montagem das listas
lista_url_sites_palavras_pais=["BR"]
lista_url_sites_palavras_cidades = ["barbacena","ceara","PraiaGrande"
                                    ,"Santos","SãoPaulo","\RIO"
                                    ,"Riojaneiro","rio-de-janeiro","Riodejaneiro","porto-alegre"]
lista_url_sites_palavras_uf = ["\SP","_sp","_rj","\RJ","rs/"]
lista_url_sites_palavras_tiparq=["/imagem/","/doc/"]

while True:             #MONTA A LISTA DE ANOS
      if ano == ano_corrente:
            break
      ano += 1
      lista_url_sites_palavras_ano.append(str(ano))

lista_url_sites_palabras_correlacionadas = ["resultados", "resultado"
    , "esporte" , "esportes", "campeonato", "campea"
    , "esportiva" , "esportivas", "etapa", "etapas"
    , "atletas", "atleta", "premiação", "premiações"
    , "endurance", "olinpico", "destaque", "resultado"
    ,"clubes","cob","mundial","doping","medalhista","pan"
    ,"pannamericano","ouro","prata", "bronze"
    ,"ouro","torneio", "jogos","jebs"]
lista_url_sites_palabras_esporte = ["corrida", "natação"
    , "bike", "ciclismo", "maratona", "triathlon"
    , "biatlhon", "duatlhom", "runner", "meia", "marathon"
    ,"basquete", "AQUATHLON","futebol"
    ,"Ironman", "swimming","ginastica-ritmica"
    ,"ginastica", "ritmica"]

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
    else:
        print(f"#### {resultado}")
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
