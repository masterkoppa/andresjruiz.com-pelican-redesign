#!/usr/bin/env python
# -*- coding: utf-8 -*- #

PLUGINS = ['pelican.plugins.gravatar', 'pelican.plugins.github_activity']

AUTHOR = u'Andres J Ruiz'
SITENAME = u'Small Thoughts'
SITEURL = 'http://andresjruiz.com'
DISQUS_SITENAME = u'andresjruiz'
AUTHOR_EMAIL = u'andresruiz2010@gmail.com'
PDF_GENERATOR = True

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'


# Social widget
SOCIAL = (('LinkedIn', 'http://www.linkedin.com/pub/andres-ruiz-torres/40/140/575'),
          ('Github', 'https://github.com/masterkoppa'))

#Must allways be a local link - USE LINKS FOR EXTERNAL STUFF
MENUITEMS = (('About Me', 'AboutMe.html'),)# ('Github Activity', 'GithubActivity.html'))
TEMPLATE_PAGES = { '../templates/AboutMe.html' : 'AboutMe.html',
					'../templates/GithubActivity.html' : 'GithubActivity.html',
					'../templates/Experience/Java.html' : 'Experience/Java.html',
					'../templates/Experience/Python.html' : 'Experience/Python.html',
					'../templates/Experience/HTML-JS.html' : 'Experience/HTML-JS.html',
					'../templates/Experience/C-C++.html' : 'Experience/C-C++.html'}

DEFAULT_PAGINATION = 3
# The number of characters to make the index page summary for each
# blog entry
DEFAULT_TRUNCATE = 500

THEME = u'bootstraped'
NON_GENERIC_BOOTSTRAP = "simplex"
GITHUB_ACTIVITY_FEED = 'https://github.com/masterkoppa.atom'