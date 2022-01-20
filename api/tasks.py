from __future__ import absolute_import, unicode_literals
from googleapiclient.discovery import build
from datetime import datetime, timedelta, timezone

from celery import shared_task

from django.db import IntegrityError
from yt_crawler import settings
from .models import VideosInfo


"""
Cron job executing in every 300 seconds.
"""
@shared_task 
def yt_crawl_job(*args, **kwargs):
    api_keys = settings.API_KEYS
    utc_time = datetime.utcnow() + timedelta(minutes=-5)
    req_time = str(utc_time.replace(tzinfo=timezone.utc)).split(' ')
    req_search_time = f'{req_time[0]}T{req_time[1][:-6]}Z'

    #Multiple Api keys, if in case key quota gets full.
    for api_key in api_keys:
        try:
            service = build('youtube', 'v3', developerKey=api_key)
            request = service.search().list(
                                            part="snippet", 
                                            order="date", 
                                            maxResults=50,
                                            publishedAfter=req_search_time,
                                            q="comedy"
                                        )
            response = request.execute()
            items = response['items']
            # print(items)
            for item in items:
                try:
                    if item['id']['videoId']:
                        video_id = item['id']['videoId']
                        published_on = item['snippet']['publishedAt']
                        title = item['snippet']['title']
                        description = item['snippet']['description']
                        thumbnail_url = item['snippet']['thumbnails']['default']['url']
                        channel_id = item['snippet']['channelId']
                        channel_title = item['snippet']['channelTitle']
                        VideosInfo.objects.create(
                            video_id=video_id,
                            title=title,
                            description=description,
                            channel_id=channel_id,
                            channel_title=channel_title,
                            published_on=published_on,
                            thumbnail_default_url=thumbnail_url,
                        )
                except IntegrityError as e:
                    continue
            break

        except:
            continue

