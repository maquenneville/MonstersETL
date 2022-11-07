# MonstersETL

for Windows


Extracts info about 2000+ Dungeons and Dragons monsters, cleans it then loads it to a PostgreSQL database.

Monster data scraped from https://www.dandwiki.com/wiki/5e_Monsters.

Built primarily with Scrapy, the first step uses a spider to crawl the target site, then uses a custom pipeline and item to clean and parse the responses from each link, writing each as rows to a CSV.  The second step uses Pandas to do some light cleaning, auto-generates SQL CREATE and COPY statements, then uses psycopg2 to load the CSV into a PostgreSQL database detailed in your database.ini file.

This is my first Scrapy project, so I decided to choose something fun.  I attempted to scrape every individual tag for each feature, but it was more effective to simply scrape all the text from the beast card and parse it after with the pipeline.  The skills I'd like to improve on this are easier techniques for custom string parsing (possibly with more extensive regexes), and overall increasing my understnding of Scrapy.

How to use:

- requires pandas, re, scrapy, psycopg2, lxml
- download all files to desired folder, and include a database.ini file with the format

[postgresql]
host=##### 
database=##### 
user=##### 
password=#####

- from command line, run scrapy runspider monster_spider.py
- then, run monster_PP_load.py
- you should now have a couple new csvs in your folder and a table of monsters in your database

Notes:

- I installed all of my packages through Anaconda prompt, and ran them through it. Results may differ if using the main Windows command line.

