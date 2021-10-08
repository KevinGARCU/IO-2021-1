from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

consumer_key = '0IGXEl2ORYCkWiHFMZGYSTGaF'
consumer_secret = 'ZF0cGYEiBAK4XX3epfx0Bx5dHAxzVo2K2Oz6h6SW5hoQnPDv18'

access_token = '1444837101078450181-hj5Gdbmwezne0rBeoKSuSgr7tXEV1a'
access_token_secret = 'hxd9H5psQS29vDJyRInDgZ4ZQdyFjz6vlUMOvxnum4Kgq'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        

        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})

app.run()