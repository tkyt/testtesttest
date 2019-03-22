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
# THEME = './themes/zurb-F5-basic'
THEME = os.path.join(
    PELICANDIR
    , 'pelican-themes'
    , 'medius'
)
# THEME = './themes/aboutwilson'
# THEME = './themes/elegant'
# THEME = './themes/svbtle'
# THEME = './themes/SoMA'

PLUGIN_PATHS = [
    os.path.join(
        PELICANDIR
        , 'pelican-plugins'
    )
]
PLUGINS = ['render_math']

AUTHOR = 'tkyt'
SITENAME = 'Test pelican on GitHub pages'
SITEURL = 'https://tkyt.github.io/testtesttest'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
