import eel
import desktop
from common import multi_thread
import common.amazon_scraping as ama
import common.twitter_api as twitter
from dotenv import load_dotenv
import os

app_name = "web"
end_point = "index.html"
size = (600,700)
thread_list = {}

load_dotenv()
ACCOUNT = {
    "consumer_key": os.getenv('CONSUMER_KEY'),
    "consumer_secret": os.getenv('CONSUMER_SECRET'),
    "access_token": os.getenv('ACCESS_TOKEN'),
    "access_token_secret": os.getenv('ACCESS_TOKEN_SECRET'),
}
my_twitter = twitter.Twitter_api(ACCOUNT)

@ eel.expose
def get_item_list(search_keyword):
    return ama.get_amazon_items(search_keyword, 1)

@ eel.expose
def check_and_tweet(items):
    new_items = list(set(items) - set(thread_list.keys()))
    remove_items = list(set(thread_list.keys()) - set(items))
    
    for remove_item in remove_items:
        thread_list[remove_item].check_status = False
        thread_list[remove_item].join()
        del thread_list[remove_item]
    
    for new_item in new_items:
        t = multi_thread.multiThread(new_item, 60, True, my_twitter)
        t.start()
        thread_list[new_item] = t

    # print(thread_list.keys())

desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)

# if __name__ == "__main__":
#     pass
