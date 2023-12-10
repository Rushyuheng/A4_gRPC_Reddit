from client import RedditClient

class HighLevel:

    def retrieve_post(self, client: RedditClient, post_id:int):
        client.start_connection()
        post = client.get_post(post_id)
        return post

    def retrieve_most_upvote_comment(self, client: RedditClient, post_id:int):
        client.start_connection()
        comment = client.get_most_upvote_comment(post_id, 1)
        return comment

    def expand_most_upvote_comment(self, client: RedditClient, post_id:int):
        client.start_connection()

    #def return_most_upvote_reply():