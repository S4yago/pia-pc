import requests
import lxml.html as html
import os
import datetime


def news(arg1):
    if arg1 == 'larepublica':
        la_republica = {'HOME_URL': 'https://www.larepublica.co/', 'XPATH_LINK_TO_ARTICLE': '//text-fill[not(@class)]/a/@href',
         'XPATH_TITLE': '//div[@class="mb-auto"]/text-fill/span/text()', 'XPATH_SUMMARY': '//div[@class="lead"]/p/text()', 'XPATH_BODY': '//div[@class="html-content"]/p[not(@class)]/text()'}
        return la_republica
    elif arg1 == 'diario':
        diario = {'HOME_URL': 'https://www.diario.mx/', 'XPATH_LINK_TO_ARTICLE': '//article[@class="rcm12 padding_0 separacion_b"]/a/@href',
         'XPATH_TITLE': '//h1[@class="titulo_1 size_ex fuente_titulos"]/text()', 'XPATH_SUMMARY': '//h2[@class="texto_3 size_big_ligh"]/text()', 'XPATH_BODY': '//div[@class="rcm12 padding_0 separacion_grande contenido_nota_parrafo"]/p[not(@class)]/text()'}
        return diario


def parse_notice(link, today, arg1):
    XPATH_TITLE = news(arg1)['XPATH_TITLE']
    XPATH_SUMMARY = news(arg1)['XPATH_SUMMARY']
    XPATH_BODY = news(arg1)['XPATH_BODY']
    try:
      response = requests.get(link)
      if response.status_code == 200:
        notice = response.content.decode('utf-8')
        parsed = html.fromstring(notice)
        try:
          title = parsed.xpath(XPATH_TITLE)[0]
          title = title.replace('\"', '')
          summary = parsed.xpath(XPATH_SUMMARY)[0]
          body = parsed.xpath(XPATH_BODY)
        except IndexError:
          return

        with open('./data/{}/{}.txt'.format(today, title), 'w', encoding='utf-8') as f:
          f.write(title)
          f.write('\n\n')
          f.write(summary)
          f.write('\n\n')
          for p in body:
            f.write(p)
            f.write('\n')
      else:
        raise ValueError(response.status_code)
    except ValueError as e:
      print(e)


def parse_home(arg1):
    HOME_URL = news(arg1)['HOME_URL']
    XPATH_LINK_TO_ARTICLE = news(arg1)['XPATH_LINK_TO_ARTICLE']
    try:
      response = requests.get(HOME_URL)
      if response.status_code == 200:
        home = response.content.decode('utf-8')
        parsed = html.fromstring(home)
        links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
        today = datetime.date.today().strftime('%Y-%m-%d')
        if not os.path.exists(f"./data/{today}"):
          os.mkdir(f"./data/{today}")
        for link in links_to_notices:
          parse_notice(link, today, arg1)
      else:
        raise ValueError(response.status_code)
    except ValueError as e:
      print(e)


def run(arg1):
    parse_home(arg1)
    if arg1 == 'larepublica':
        web = "www.larepublica.co"
    else:
        web = "www.diario.mx"
    print(f"[+] Tarea finalizada! Se han descargado las noticias correspondientes al sitio web de {web}")