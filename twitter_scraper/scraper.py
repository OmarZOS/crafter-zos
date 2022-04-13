import os
import snscrape.modules.twitter as sntwitter
import networkx as nx
from networkx.readwrite import json_graph
import json
from constants import *
import pika
from pika.exchange_type import ExchangeType
# Creating list to append tweet data to

# graph = nx.DiGraph()
# graph.add_edges_from()
# graph.add

    




def add_user_node(user,graph):
    graph.add_nodes_from([(user.id,{
            "id":user.id,
            "username":user.username,
            "displayname":user.displayname         ,
            "description":user.description         ,
            "rawDescription":user.rawDescription          ,
            "descriptionUrls":user.descriptionUrls         ,
            "verified":user.verified,
            "created": user.created.strftime("%Y-%m-%d, %H:%M:%S") if user.created  else "",
            "followersCount":user.followersCount,
            "friendsCount":user.friendsCount,
            "statusesCount":user.statusesCount,
            "favouritesCount":user.favouritesCount,
            "listedCount":user.listedCount,
            "mediaCount":user.mediaCount,
            "location":user.location,
            "protected":user.protected,
            "linkUrl":user.linkUrl,
            "linkTcourl":user.linkTcourl,
            "profileImageUrl":user.profileImageUrl,
            "profileBannerUrl":user.profileBannerUrl,
            "label":str(user.label),
            "node_type":"user"
        })])

def add_tweet_node(tweet,graph):
    
    graph.add_nodes_from([(tweet.id,{
        "id":tweet.id,
        "url":tweet.url,
        "date":tweet.date.strftime("%Y-%m-%d, %H:%M:%S"),
        "content":tweet.content,
        "retweetCount":tweet.retweetCount,
        "url":tweet.url,
        "replyCount":tweet.replyCount,
        "retweetCount":tweet.retweetCount,
        "likeCount":tweet.likeCount,
        "quoteCount":tweet.quoteCount,
        "conversationId":tweet.conversationId,
        "lang":tweet.lang,
        "source":tweet.source,
        "sourceUrl":tweet.sourceUrl,
        "sourceLabel":tweet.sourceLabel,
        "outlinks":str(tweet.outlinks),
        "tcooutlinks":str(tweet.tcooutlinks),
        # "media":tweet.media,
        # "retweetedTweet":tweet.retweetedTweet,
        # "quotedTweet":tweet.quotedTweet,
        "coordinates":str(tweet.coordinates),
        "place":str(tweet.place),
        "node_type": "tweet"
        })])
    
def add_media_node(url,graph):
    graph.add_nodes_from([(url,{
        "url":url,
        "node_type":"media"
    })])


def add_hashtag_node(hashtag,graph):
    graph.add_nodes_from([(hashtag,{
        "text":hashtag,
        "node_type":"hashtag"
    })])

def add_tweet_node_id(id,graph):
    graph.add_nodes_from([(id,{"id":id,
    "node_type":"tweet"}
    )])
    

def process_data(t_list,graph=nx.DiGraph()):
    for tweet in t_list:

        add_user_node(tweet.user,graph)
        add_tweet_node(tweet,graph)
        
        graph.add_edge(tweet.user.id,tweet.id)
        # graph[tweet.user.id][tweet.id]["edge_type"] = "tweeted"
        attrs = {(tweet.user.id,tweet.id): {"edge_type":"tweeted"}}
        nx.set_edge_attributes(graph, attrs)
        if tweet.inReplyToTweetId:
            add_tweet_node_id(tweet.inReplyToTweetId,graph)
            graph.add_edge(tweet.id,tweet.inReplyToTweetId)
            # graph[tweet.id][tweet.inReplyToTweetId]["edge_type"] = "inReplyToTweetId"
            attrs = {(tweet.id,tweet.inReplyToTweetId): {"edge_type":"inReplyToTweetId"}}
            nx.set_edge_attributes(graph, attrs)
        
        if tweet.inReplyToUser:
            graph.add_edge(tweet.id,tweet.inReplyToUser.id)
            attrs = {(tweet.id,tweet.inReplyToUser.id): {"edge_type":"inReplyToUser"}}
            nx.set_edge_attributes(graph, attrs)

        if tweet.mentionedUsers :
            for mentioned_user in tweet.mentionedUsers:
                add_user_node(mentioned_user,graph)
                graph.add_edge(tweet.id,mentioned_user.id)
                # graph[tweet.id][mentioned_user.id]["edge_type"] = "mentioned_user"
                attrs = {(tweet.id,mentioned_user.id): {"edge_type":"mentioned_user"}}
                nx.set_edge_attributes(graph, attrs)
        
        if tweet.hashtags :
            for hashtag in tweet.hashtags:
                add_hashtag_node(hashtag,graph)
                graph.add_edge(tweet.id,hashtag)
                attrs = {(tweet.id,hashtag): {"edge_type":"contains_hashtag"}}
                nx.set_edge_attributes(graph, attrs)

        if tweet.retweetedTweet:
            add_tweet_node(tweet.retweetedTweet,graph)
            graph.add_edge(tweet.id,tweet.retweetedTweet)
            # graph[tweet.id][tweet.inReplyToTweetId]["edge_type"] = "inReplyToTweetId"
            attrs = {(tweet.id,tweet.retweetedTweet): {"edge_type":"retweet_of"}}
            nx.set_edge_attributes(graph, attrs)
                    
        if tweet.quotedTweet:
            add_tweet_node(tweet.quotedTweet,graph)
            graph.add_edge(tweet.id,tweet.quotedTweet.id)
            # graph[tweet.id][tweet.inReplyToTweetId]["edge_type"] = "inReplyToTweetId"
            attrs = {(tweet.id,tweet.quotedTweet.id): {"edge_type":"quote_of"}}
            nx.set_edge_attributes(graph, attrs)
            

        if tweet.media:
            # print(tweet.media)
            for k in tweet.media:
                if (type(k).__name__=="Photo"):
                    add_media_node(k.fullUrl,graph)
                    attrs = {(tweet.id,k.fullUrl): {"edge_type":"contains_media"}}
                    nx.set_edge_attributes(graph, attrs)
                if (type(k).__name__=="Video"):
                    add_media_node(k.thumbnailUrl,graph)
                    attrs = {(tweet.id,k.thumbnailUrl): {"edge_type":"contains_media"}}
                    nx.set_edge_attributes(graph, attrs)

    return graph
        # inReplyToTweetId
        # inReplyToUser

        # graph
    
def search_twitter(query):
    # Using TwitterSearchScraper to scrape data and append tweets to list
    local_list=[]
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        
        # if i%CHUNK_SIZE == 0:
        #     process_data(local_list)
        #     local_list=[]
        if i > TWEET_LIMIT:
        #     process_data(local_list)
            break    #.date, tweet.id, tweet.content, tweet.user.username,tweet.user.id
        
        # print(tweet.id)
        # print(tweet.user.id)
        local_list.append(tweet)
        
    return local_list

def save_json(filename,graph):
    g = graph
    g_json = json_graph.node_link_data(g)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    json.dump(g_json,open(filename,'a+'),indent=2)

def twitter_trends(query):
    # Using TwitterSearchScraper to scrape data and append tweets to list
    local_list=[]
    for i,tweet in enumerate(sntwitter.TwitterTrendsScraper().get_items()):
        
        # if i%CHUNK_SIZE == 0:
        #     self.process_data(local_list)
        #     local_list=[]
        
        if i > TWEET_LIMIT:
            # self.process_data(local_list)
            break    #.date, tweet.id, tweet.content, tweet.user.username,tweet.user.id
        
        # print(tweet.id)
        # print(tweet.user.id)
        local_list.append(tweet)
        
    return local_list

def init_publisher(user,password,exchange):
    credentials = pika.PlainCredentials(user,password)
    connection= pika.BlockingConnection(pika.ConnectionParameters(host=RMQ_HOST,credentials=credentials))#, credentials= self.credentials
    channel= connection.channel()
    channel.exchange_declare(exchange=exchange, exchange_type=ExchangeType.direct)

def publish_data(args):
    pass

if __name__=="__main__":

    keyword = "الجزائر"
    from_date="2021-01-01"
    to_date="2022-04-06"

    graph = nx.DiGraph()
    # scraper = TwitterSearcher()
    data = search_twitter(f'{keyword} since:{from_date} until:{to_date}')
    
    graph = process_data(data)

    # print([k.hashtags for k in data])
    # print(scraper.graph.nodes)
    save_json("somewhere",graph)
