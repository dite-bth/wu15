from flask import Flask, render_template, request
import twitter, pprint

app = Flask(__name__)


# Create a API object
api = twitter.Api(consumer_key=TWITTER_COMSUMER_KEY,
                  consumer_secret=TWITTER_COMSUMER_SECRET,
                  access_token_key=TWITTER_ACCESS_TOKEN_KEY,
                  access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

# Set up a pretty printer for console output
pp = pprint.PrettyPrinter(indent=4)


# Main route (root)
@app.route('/')
def start_page():
    # Look for GET-arguments
    if 'tweet_search' in request.args:
        search_word = request.args.get('tweet_search', '')
    else:
        search_word = 'skate'  # Set "skate" as default search word

    # Use Twitter API to search for tweets
    result = api.GetSearch(search_word)

    # Print data to console
    for tweet in result:
        pp.pprint(tweet)

    # Render template index.html (pass data to template)
    return render_template("index.html", search_word= search_word, tweets=result)


if __name__ == '__main__':
    app.run()
