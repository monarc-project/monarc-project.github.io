#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = '"security made in Lëtzebuerg" (SMILE) g.i.e.'
SITENAME = 'MONARC'
SITEURL = '.'

THEME = "./themes/pelican-bootstrap3"
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['i18n_subsites']
FEED_ALL_ATOM = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_MENU = False


PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('CASES', 'https://www.cases.lu'),
         ('security made in Lëtzebuerg', 'https://securitymadein.lu'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/CASES-LU'),
          ('Twitter', 'https://twitter.com/cases_lu'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
