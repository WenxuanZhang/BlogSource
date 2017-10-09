#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Wenxuan Zhang'
SITENAME = u"Unlocking the Power of Data"
SITEURL = 'https://wenxuanzhang.github.io'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "pelican-themes/voidy-bootstrap"
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['assets']

# Adding Side Bar
SIDEBAR = "sidebar.html"
CUSTOM_SIDEBAR_MIDDLES = ("sb_links.html", "sb_taglist.html", )
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
SITESUBTITLE ='Exploring Business Solutions'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'))

# Social widget
#SOCIAL = (('github', 'https://github.com/WenxuanZhang'),
#          ('linkedin', 'https://www.linkedin.com/in/wenxuanzhang5/'),
#          ('twitter','https://twitter.com/ZhangWenxuan1'),
#          ('blog','https://wenxuandatascientist.blogspot.com/'))



# Extra stylesheets, for bootstrap overrides or additional styling.
STYLESHEET_FILES = ("pygment.css", "voidybootstrap.css",)

# Put taglist at end of articles, and use the default sharing button implementation.
CUSTOM_ARTICLE_FOOTERS = ("taglist.html", "sharing.html", )
CUSTOM_SCRIPTS_ARTICLE = "sharing_scripts.html"

# Default sidebar template. Omit this setting for single column mode without sidebar.

SOCIAL = (('Google+', 'https://wenxuandatascientist.blogspot.com/',
         'fa fa-google-plus-square fa-fw fa-lg'),
        ('Twitter', 'https://twitter.com/ZhangWenxuan1',
         'fa fa-twitter-square fa-fw fa-lg'),
        ('LinkedIn', 'http://linkedin-url',
         'fa fa-linkedin-square fa-fw fa-lg'),
        ('GitHub', 'https://github.com/WenxuanZhang',
         'fa fa-github-square fa-fw fa-lg'),
        )


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
