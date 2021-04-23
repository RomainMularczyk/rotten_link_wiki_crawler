#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mongoengine


# In[3]:


class WikiUrls(mongoengine.Document):
    original_url = mongoengine.StringField(required=True)
    current_url = mongoengine.StringField(required=True)
    status_code = mongoengine.StringField(required=True)
    date_crawl = mongoengine.DateField(required=True)
    
    meta = {'db_alias': 'core',
            'collection': 'wiki_urls'}

