import snscrape.modules.twitter as sntwitter
import pandas as pd
import json

# Using TwitterSearchScraper to scrape data and append tweets to list (BUS)
tweets_list2 = []

for i,tweet in enumerate(sntwitter.TwitterSearchScraper('One-North since:2016 until:2021-02-08').get_items()):
    if i>3000:
        break
    tweets_list2.append([str(tweet.date), tweet.id, tweet.content, tweet.username])
    
# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

result = tweets_df2.to_json(orient="split")
parsed = json.loads(result)
final = json.dumps(parsed, indent=4)

with open('twitter_newOverall_data.py', 'w') as f: 
    f.write(final)