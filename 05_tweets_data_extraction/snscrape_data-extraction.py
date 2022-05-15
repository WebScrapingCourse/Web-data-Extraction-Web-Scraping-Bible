import snscrape.modules.twitter as sntwitter
import psycopg2
from dao import insert_data
from utils import load_conf, api_search

def snscrape_extractor(  hashtag, start_date, end_date):
    tweets = sntwitter.TwitterSearchScraper(hashtag+" since:"+start_date+" until:"+end_date).get_items()
    return [[t.id,
                 t.date.isoformat()[0:10],t.user.username,
                 t.user.location or "None",t.user.friendsCount,
                 t.user.followersCount,t.retweetCount,
                 t.content] for t in tweets]

if __name__ == "__main__":

    # Connect to PostgreSQL
    conn_info = load_conf("postgresql")
    connection = psycopg2.connect(**conn_info)

    # Insert data into the tweets table
    columns='id, time, username, location, following, followers, retweetcount, text'
    hashtag, start_date, end_date = "#Ucraina", "2022-03-01", "2022-03-02"
    values_list = snscrape_extractor( hashtag, start_date, end_date)
    print("Start sending to Postgres")
    for values in values_list:
        insert_data(connection, columns, values)

    # Close all connections to the database
    connection.close()
