#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'security made in Lëtzebuerg (SMILE) g.i.e.'
SITENAME = 'MONARC'
SITEURL = 'http://monarc.lu/'
PATH = 'content'
# PAGE_PATHS = ['pages']
# ARTICLE_PATHS = ['news']
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'
TYPOGRIFY = True
#PAGE_ORDER_BY = 'sortorder'
STATIC_PATHS = ['assets', 'administrator-guide', 'technical-guide',
                'quick-start', 'user-guide', 'method-guide',
                'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
SITELOGO = 'assets/images/monarc-logo.png'
SITELOGO_SIZE = '20px'
FAVICON = 'assets/images/monarc-logo.png'
THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'cerulean'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites']
DEFAULT_PAGINATION = 10
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
BOOTSTRAP_FLUID = False
BOOTSTRAP_NAVBAR_INVERSE = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
CC_LICENSE = "CC-BY-SA"

READERS = {"html": None}

# Navbar
MENUITEMS = (
        ('News', '/archives'),
        ('Documentation', '/documentation'),
        ('Community', '/community'),
        ('Download', '/download'),
        ('Trainings', '/trainings'),
)

# Links
LINKS = (('MONARC <i>Cloud</i>', 'https://my.monarc.lu/'),
         (' CASES', 'https://www.cases.lu/monarc.html'),
         ('Cybersecurity Competence Center (C3)', 'https://c-3.lu'),
         ('SECURITYMADEIN.LU', 'https://securitymadein.lu'),
         ('<img src="https://img.shields.io/github/release/monarc-project/MonarcAppFO.svg?style=flat-square" />',
            'https://github.com/monarc-project/MonarcAppFO/releases/latest'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/monarc-project'),
          ('Twitter', 'https://twitter.com/cases_lu'),
          ('RSS', FEED_DOMAIN + FEED_ALL_ATOM),)

NAVBAR_ELEMENTS = ['menu-items']

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
PATH_METADATA= '(?P<path_no_ext>.*)\..*'
ARTICLE_URL = 'news/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'news/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = os.path.join(PAGE_URL, 'index.html')
# PAGE_SAVE_AS = '{path_no_ext}.html'
# PAGE_URL = '{path_no_ext}.html'
