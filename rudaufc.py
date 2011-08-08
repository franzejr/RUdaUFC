#!/usr/bin/python
# -*- encoding: utf-8 -*-
# rudaufc.py
# 03/08/2011
# 08/08/2011 - indentacao, headers python, ImportError handler
# @lelimat / @franzejr / @silveira

import twitter, sys
from datetime import datetime

# Dados da API do @rudaufc
oauth_token = ''
oauth_token_secret = ''
consumer_key = ''
consumer_secret = ''

api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=oauth_token, access_token_secret=oauth_token_secret)

semana = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex']

try:
    from lxml.html import parse
except ImportError:
    print "lxml module not found. tip: sudo apt-get install python-lxml"
else:
    now = datetime.now()
    dia_da_semana = datetime.weekday(now)

    links = {'Vegetariano':'http://www.ufc.br/portal/index.php?option=com_content&task=view&id=6759&Itemid=87',
             'Comum'      :'http://www.ufc.br/portal/index.php?option=com_content&task=view&id=11650&Itemid=87'}

    for link in links.keys():
        cardapio = []
        page = parse(links[link]).getroot()
        for i in page.cssselect('ul li strong'):
            if not i.text.lower().startswith('aten') and i.text.strip() != '':
                cardapio.append(i.text)
        tweet = link + ' (' + semana[dia_da_semana] + '): ' + cardapio[dia_da_semana]
        status = api.PostUpdate(tweet[:140])
        #print tweet
