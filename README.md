# Este projeto é uma solução que recupera na WEB as informações esportivas de uma pessoa.  
 
    #FASE 1 - Procurando na web - Utilizando a bibliotea googlesearch
            #FASE 1.1 - Iniciado
              Filtros das pesquisas atraves do nome e cpf
              Validação dos sites cujos os links não estão mais funcionando          
              A)Obter informações nas urls:                               
                    Pais, estado e cidade;
                    Ano do evendo;
                    Sites dos organizadores das provas;
                    tipo de arquivo
                    palavras correlacionadas,exemplos: olimpico, premio, ouro, cob, prova, etc.
               B)consolidar informações obtidas na url - Não iniciado
               C)CLASSES CONSTRUIDAS PARA ATENDER A FASE 1.1
                 #class raspa_url:
                      #def separa_url(site1,ano,lista_url_sites_palabras_esporte):   #obtem o endereço absoluto do site.
                      #def separa_url_generico(site1, lista,tipo):                   #obtem informações contidas na url  pais, uf, etc.
                 #class consolida_url:
                      #def soma_resultado(v_tipo,v_lista):                           #totalização por tipo de informação pais, uf, etc.
                 #class valida_site:
                      #def tipo(site1):                                              # filtra o tipo de site 
                      #def existe(site1):                                            # verifica se o site esta acessivel           
     #FASE 1.2 - Não iniciado
              Ler o HTML dos sites e extraindo as informações: inscrições, resultados de provas e etc.
              Resultados, categoria, tempos, local das provas e etc.
              Confirmar as informações obtidas da fase 1.1 (
                Os sites correlacionadosos tipos(esportes, buscadores de informações, juridicos, redes sociais, etc.)                
                    Pais
                    Ano.
              
              Filtros das pesquisas estão em definição.
    #FASE 2 - Analise - Não iniciado
          Tendencia de compras
          Tendencia de esportes


