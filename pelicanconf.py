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
    , 'cebong'
    #, 'Just-Read'
    #, 'nikhil-theme'
    #, 'pelican-hss'
)
PLUGIN_PATHS = [
    os.path.join(
        PELICANDIR
        , 'pelican-plugins'
    )
]
PLUGINS = ['render_math']

AUTHOR = 'tkyt'
SITENAME = 'Test pelican on GitHub pages'
SITEURL = 'http://localhost:8000'
SITEURL = 'https://tkyt.github.io/testtesttest'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

DEFAULT_CATEGORY = 'misc'

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

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

