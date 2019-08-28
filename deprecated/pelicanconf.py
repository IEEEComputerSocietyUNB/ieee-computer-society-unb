#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'IEEE Computer Society UnB'
SITENAME = 'IEEE Computer Society UnB'
SITEURL = ''

# Customized settings
THEME = 'bulrush/bulrush'
LOAD_CONTENT_CACHE = False

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt-br'

ARTICLE_PATHS = ['articles', ]
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social
GITHUB_URL = 'http://getpelican.com/'
TWITTER_URL = 'http://getpelican.com/'
FACEBOOK_URL = 'http://getpelican.com/'

# Blogroll
LINKS = (('Facebook', 'http://getpelican.com/'),
         ('Github', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Facebook', 'http://getpelican.com/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
