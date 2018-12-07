#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "aldi"
SITENAME = "kriwil.id"
SITEURL = ""

PATH = "content"

TIMEZONE = "Asia/Jakarta"

THEME = "themes/kriwil.id"
DEFAULT_LANG = "id"

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["assets", "custom_article_urls", "sitemap"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (("kriwil.com", "https://kriwil.com/"),)

# Social widget
SOCIAL = (("twitter", "https://twitter.com/kriwil"),)

DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

SITEMAP = {
    "format": "xml",
    "changefreqs": {"articles": "daily", "pages": "daily", "indexes": "daily"},
    "exclude": ["tag/", "category/"],
}

CUSTOM_ARTICLE_URLS = {
    "links": {
        "URL": "{category}/{date:%Y%m%d}/{slug}/",
        "SAVE_AS": "{category}/{date:%Y%m%d}/{slug}/index.html",
    }
}
