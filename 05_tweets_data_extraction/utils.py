import tweepy
from configparser import ConfigParser

def load_conf(config_name):
    parser = ConfigParser()
    parser.read("config.ini")

    # Create a dictionary of the variables stored under the "postgresql" section of the .ini
    conn_info = {param[0]: param[1] for param in parser.items(config_name)}
    return conn_info

def api_search(conf):
    auth = tweepy.OAuthHandler(
        conf["consumer_key"],
        conf["consumer_secret"])
    auth.set_access_token(
        conf["access_token"],
        conf["access_token_secret"])
    return tweepy.API(auth).search


