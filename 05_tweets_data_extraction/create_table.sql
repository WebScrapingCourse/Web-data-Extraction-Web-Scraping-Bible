CREATE TABLE IF NOT EXISTS tweets(
    id BIGINT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    location VARCHAR(100) NOT NULL,
    following INTEGER,
    followers INTEGER,
    retweetcount INTEGER,
    text VARCHAR(100000) NOT NULL
)


