#!/usr/bin/python
# -*- encoding: utf-8 -*-
# rudaufc.py
# 03/08/2011
# 23/08/2011 - indentacao, headers python, ImportError handler
# @lelimat / @franzejr / @silveira

import twitter, sys
from datetime import datetime
sys.path.append('/home/sorteamos/svn.sorteamos.com.br/libs/lxml-2.3/build/lib.linux-x86_64-2.5')

# Dados da API do @rudaufc
oauth_token = '80696879-JDbn8frBA5AInwl9c2LJFXJr6rTxG0ldbWtzSKSg8'
oauth_token_secret = '9e41CzLVU8W3RBp9KOoUjes1diW5MpDkirHjBGv4mC8'
consumer_key = 'vuPoj70EgwiwTSCsUfn7WQ'
consumer_secret = '7WWawEvQf79HWPzHTeLoAZRMbX2xni5fM7ZUISIrXQ'

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
        for i in page.cssselect('td ul li'):
            text = ''
            for t in i.getchildren():
                #print t
                if t.tag == 'strong':
                    text = text + ' ' + t.text.strip()
            #print text
            text = text.strip()
            if not text.lower().startswith('aten') and text != '':
                cardapio.append(text)
        tweet = link + ' (' + semana[dia_da_semana] + '): ' + cardapio[dia_da_semana]
        status = api.PostUpdate(tweet[:140])
        #print tweet
