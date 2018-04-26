# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import New
from django.shortcuts import render,render_to_response
import json
# Create news views. get request and new information
def display_news(request):
    all_news = New.objects.all()
    news_listing = []
    for news in all_news:
        news_dict = {}
        news_dict['news_title']= news.n_title
        news_dict['news_context'] = news.n_content
        news_dict['news_date'] = news.n_date
        news_listing.append(news_dict)
    return render_to_response('quiz/news.html', {'news_list': news_listing})