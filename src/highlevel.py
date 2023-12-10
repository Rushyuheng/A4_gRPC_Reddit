from client import RedditClient

class HighLevel:

    def retrieve_post(self, client: RedditClient, post_id:int):
        client.start_connection()
        post = client.get_post(post_id)
        return post

    def retrieve_most_upvote_comment(self, client: RedditClient, post_id:int):
        client.start_connection()
        comment = client.get_most_upvote_comment(post_id, 1)

        if(len(comment) == 0):
            return None

        return comment[0]

    def expand_most_upvote_comment(self, client: RedditClient, post_id:int):
        client.start_connection()
        comment = client.get_most_upvote_comment(post_id, 1)

        # return None if there is no comment under the post 
        if(len(comment) == 0):
            return None
        comment = comment[0]
        
        expand_comments = client.expand_branch(comment.comment_id,5)

        # return None if the most upvote comment has no comment under that 
        if len(expand_comments) == 0:
            return None

        return expand_comments

    #def return_most_upvote_reply():