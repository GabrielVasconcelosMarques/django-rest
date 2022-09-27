from django.http import JsonResponse
from django.shortcuts import render
import requests
import json

def get_conteudo_html(produto):
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    produto = produto.replace(" ", "+")
    html_content = session.get(f'https://www.drogasil.com.br/search?w={produto}').text
    return html_content

def produtos(request, nome_do_produto):
    if request.method == "GET":
        lista_nome = None
        lista_img = None
        lista_preco = None
        lista_tarja = None
        lista_conjunta = None
        
        html_content = get_conteudo_html(nome_do_produto)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')


        script = soup.find('script', {'id':'__NEXT_DATA__'})
        texto_do_script = script.string

        retorno_json = json.loads(texto_do_script)

        lista_preco = []
        lista_tarja = []
        lista_nome = []
        lista_img = []
        lista_conjunta = []

        if 'products' in retorno_json['props']['pageProps']['initialData']:

            for c in retorno_json['props']['pageProps']['initialData']['products']:
                lista_nome.append(c['name'])
                lista_img.append(c['image'])
                lista_preco.append(c['price'])
                if c['descriptionStripe'] != None:
                    lista_tarja.append(c['descriptionStripe'])
                else:
                    lista_tarja.append('PRODUTO SEM TARJA')

            for c in range(len(lista_nome)):
                lista_conjunta.append([lista_nome[c], lista_img[c], lista_preco[c], lista_tarja[c]])
            dicionario_final = {'data': lista_conjunta}



        return JsonResponse(dicionario_final)