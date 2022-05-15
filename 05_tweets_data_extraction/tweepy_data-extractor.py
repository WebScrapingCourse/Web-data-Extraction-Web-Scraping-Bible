import tweepy
import psycopg2
from dao import insert_data
from utils import load_conf, api_search

def tweepy_extractor( api_search, hashtag, start_date, end_date):
    tweets = tweepy.Cursor(api_search, q=hashtag, geocode="41.8919,12.5113,100km", lang="it", wait_on_rate_limit=True,
                           since=start_date, until=end_date, tweet_mode='extended').items()
    return [[t.id, t.created_at.isoformat()[0:10],
             t.user.screen_name, t.user.location or "None",
             t.user.friends_count, t.user.followers_count,
             t.retweet_count, t.full_text] for t in tweets]
if __name__ == "__main__":
    # Connect to Tweepy API
    conf = load_conf("tweepy")
    api = api_search(conf)

    # Connect to PostgreSQL
    conn_info = load_conf("postgresql")
    connection = psycopg2.connect(**conn_info)

    # Insert data into the tweets table
    columns='id, time, username, location, following, followers, retweetcount, text'
    hashtag, start_date, end_date = "#Ucraina", "2022-03-17", "2022-03-18"
    values_list = tweepy_extractor(api, hashtag, start_date, end_date)
    for values in values_list:
        insert_data(connection, columns, values)

    # Close all connections to the database
    connection.close()

