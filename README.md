

<div align='center'><h1>Simple reddit parser</h1></div>
<p align='center'><img src='readme_assets\img.png' height='256'/></p>


## What is that?
Simple console parser for reddit, just enter subreddit name and get: 
+ Post names wthin last three days (period is customizable,
  you can change it in app/contants.py, `CUT_OFF_TIME_DAYS` parameter)
+ Most efficient post starters
+ Most active comment authors

## Requirements
<a href='requirements.txt'>Here they are...</a>

## Project setup
+ Clone repo: `git clone https://github.com/FAV1290/reddit_parser`
+ Open repo catalog and install requirements: `pip install -r requirements.txt`
+ Sign in on reddit and get your app id and secret on https://ssl.reddit.com/prefs/apps/
+ Add environment variable or .env lines `REDDIT_APP_CLIENT_ID and REDDIT_APP_CLIENT_SECRET` with your app id and secret
+ Add environment variable or .env line `REDDIT_APP_USER_AGENT` with preferred user agent like `'pc:PostParser:v1.0 (by u/YourRedditName)'`
+ Run script: `python __main__.py`
+ You are awesome!

## How does it look?
<img src='readme_assets\screenshot1.png'/>
<img src='readme_assets\screenshot2.png'/>
<img src='readme_assets\screenshot3.png'/>
