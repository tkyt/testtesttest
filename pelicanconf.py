#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
PELICANDIR = os.path.join(
    os.environ['HOME']
    , 'mnt'
    , 'srv'
    , 'data'
    , 'pelican'
)
THEME = os.path.join(
    PELICANDIR
    , 'pelican-themes'
    #, 'clean-blog'
    #, 'cebong'
    #, 'Just-Read'
    #, 'nikhil-theme'
    , 'simple-bootstrap'
    #, 'pelican-hss'
)
THEME = 'themes/simpla-lancxo'
PLUGIN_PATHS = [
    os.path.join(
        PELICANDIR
        , 'pelican-plugins'
    )
]
PLUGINS = ['render_math']

AUTHOR = 'tkyt'
SITENAME = 'Baby learnings'
SITE_DESCRIPTION = 'to stand on the shoulders of Giants'
SITETAGLINE = 'to stand on the shoulders of Giants'
SITESUBTITLE = 'to stand on the shoulders of Giants'
SITEURL = 'http://localhost:8000'

PATH = 'content'
#ARTICLE_URL = os.path.join(
#    '{date:%Y}'
#    , '{date:%m}'
#    , '{date:%d}'
#    , '{slug}'
#)
#ARTICLE_SAVE_AS = os.path.join(
#    '{date:%Y}'
#    , '{date:%m}'
#    , '{date:%d}'
#    , '{slug}.html'
#)
OUTPUT_PATH = 'docs/'
YEAR_ARCHIVE_SAVE_AS = os.path.join(
    '{date:%Y}'
    , 'index.html'
)
MONTH_ARCHIVE_SAVE_AS = os.path.join(
    '{date:%Y}'
    , '{date:%m}'
    , 'index.html'
)

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'
DEFAULT_CATEGORY = 'misc'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
SUMMARY_MAX_LENGTH = 0

DELETE_OUTPUT_DIRECTORY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Google Japan', 'http://google.co.jp/'),
#          ('Apple Japan', 'http://apple.com/jp'),
#          ('Amazon Japan', 'http://amazon.co.jp/'))

# Social widget
# SOCIAL = (('Twitter', '#'),)

DEFAULT_PAGINATION = 10

FOOTERTEXT = 'Persona kono bazo kaj Hodiaŭ mi lernis'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

