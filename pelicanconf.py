#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import urllib.parse

AUTHOR = 'SECURITYMADEIN.LU g.i.e.'
SITENAME = 'MONARC'
SITEURL = 'https://www.monarc.lu'
RELATIVE_URLS = True
# SITEURL = 'http://127.0.0.1:8000/'
PATH = 'content'
# PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['pages/news']
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'
TYPOGRIFY = True
#PAGE_ORDER_BY = 'sortorder'
STATIC_PATHS = ['assets',
                'extra',
                'documentation/administrator-guide',
                'documentation/technical-guide',
                'documentation/quick-start',
                'documentation/user-guide',
                'documentation/method-guide',
                'documentation/MOSP-documentation',
                'documentation/stats-service']
CUSTOM_CSS = 'static/css/custom.css'
EXTRA_PATH_METADATA = {
                        'extra/CNAME': {'path': 'CNAME'},
                        'extra/custom.css': {'path': CUSTOM_CSS},
                    }
# SITELOGO = 'assets/images/monarc-logo.png'
# SITELOGO_SIZE = '20px'
FAVICON = 'assets/images/monarc-logo.png'
THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'cerulean'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites', 'sitemap']
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
CC_LICENSE = 'CC-BY-SA'

SITEMAP = {
    'format': 'txt',
    'exclude': ['tag/', 'category/'],
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.8
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

READERS = {"html": None}

MARKDOWN = {
  'extension_configs': {
    'markdown.extensions.toc': {
      'title': 'Table of contents:'
    },
    'markdown.extensions.codehilite': {'css_class': 'highlight'},
    'markdown.extensions.extra': {},
    'markdown.extensions.meta': {},
    'markdown.extensions.tables':{},
  },
  'output_format': 'html5',
}

# Navbar
MENUITEMS = (
        ('News', '/news'),
        ('Product', '/product'),
        ('Service', '/service'),
        ('Community', '/community'),
        ('Publications', '/publications'),
        ('Documentation', '/documentation'),
        ('Download', '/download'),
        ('Trainings', '/trainings'),
        ('Work with us', '/internship')
)

# Links
LINKS = (('MONARC <i>Cloud</i>', 'https://my.monarc.lu'),
         ('Objects Sharing Platform', 'https://objects.monarc.lu'),
         ('MONARC Cybersecurity Landscape', 'https://dashboard.monarc.lu'),
         ('Subscribe to the releases', 'https://open-source-security-software.net/project/MONARC/releases.atom'),
         ('CASES', 'https://cases.lu'),
         ('<img src="https://img.shields.io/github/release/monarc-project/MonarcAppFO.svg?style=flat-square" />',
            'https://github.com/monarc-project/MonarcAppFO/releases/latest'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/monarc-project'),
          ('Twitter', 'https://twitter.com/MONARCproject'),
          ('RSS', urllib.parse.urljoin(FEED_DOMAIN, FEED_ALL_ATOM)),)

NAVBAR_ELEMENTS = ['menu-items']


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
PATH_METADATA= '(?P<path_no_ext>.*)\..*'
ARTICLE_URL = 'news/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'news/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
INDEX_SAVE_AS = 'news/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = os.path.join(PAGE_URL, 'index.html')

# PAGE_SAVE_AS = '{path_no_ext}.html'
# PAGE_URL = '{path_no_ext}.html'
