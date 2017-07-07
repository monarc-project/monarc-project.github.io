#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'security made in Lëtzebuerg (SMILE) g.i.e.'
SITENAME = 'MONARC'
SITEURL = 'http://localhost:8000'
PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'
TYPOGRIFY = True
PAGE_ORDER_BY = 'sortorder'
STATIC_PATHS = ['pdfs']
SITELOGO = 'images/monarc-logo.png'
SITELOGO_SIZE = '20px'

THEME = "./themes/pelican-bootstrap3"
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['i18n_subsites']
DEFAULT_PAGINATION = 10
FEED_ALL_ATOM = True
BOOTSTRAP_FLUID = False
BOOTSTRAP_NAVBAR_INVERSE = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
CC_LICENSE = "CC-BY-SA"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Navbar
MENUITEMS = (
        ('News', '/news'),
        ('Documentation', '/pages/documentation'),
        ('Community', '/pages/community/'),
        ('Download', '/pages/download'),
        ('Trainings', '/pages/trainings'),
)

# Links
LINKS = (('CASES', 'https://www.cases.lu'),
         ('security made in Lëtzebuerg', 'https://securitymadein.lu'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/monarc-project'),
          ('Twitter', 'https://twitter.com/cases_lu'),)

NAVBAR_ELEMENTS = ['menu-items']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PATH_METADATA= '(?P<path_no_ext>.*)\..*'
ARTICLE_URL = 'news/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'news/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
# PAGE_URL = '{slug}.html'
# PAGE_SAVE_AS = '{slug}.html'
PAGE_SAVE_AS= '{path_no_ext}.html'
PAGE_URL= '{path_no_ext}.html'
