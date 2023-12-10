from client import RedditClient

class HighLevel:

    def retrieve_post(self, client: RedditClient, post_id:int):
        post = client.get_post(post_id)
        return post

    #def retrieve_most_upvote():

    #def expand_most_upvote():

    #def return_most_upvote_reply():