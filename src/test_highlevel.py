from highlevel import HighLevel
from unittest import TestCase, main
from unittest.mock import patch, Mock
from mock_db import MockDB
from reddit_service import RedditServicer


class TestHighLevel(TestCase):
    def setUp(self) -> None:
        self.system_under_test = HighLevel()
        self.mock_db = MockDB()

    # test if retrieve_post invoke correct client function with correct parameter
    def test_retrieve_post(self) -> None:
        #set up
        #create mock instance
        mock_client = Mock()
        #stub mock return
        mock_client.get_post.return_value = RedditServicer.construct_post_from_dbrecord(self.mock_db.post[0])

        #function parameter
        post_id = 0

        #execution
        self.system_under_test.retrieve_post(mock_client,post_id)

        #verify
        mock_client.get_post.assert_called_with(post_id)

    # test if retrieve_most_upvote_comment invoke correct client function with correct parameter
    def test_retrieve_most_upvote_comment(self) -> None:
        #set up
        #create mock instance
        mock_client = Mock()
        #stub mock return
        mock_client.get_most_upvote_comment.return_value = [RedditServicer.construct_comment_from_dbrecord(self.mock_db.comment[0])]

        #function parameter
        post_id = 0

        #execution
        self.system_under_test.retrieve_most_upvote_comment(mock_client,post_id)

        #verify
        mock_client.get_most_upvote_comment.assert_called_with(post_id,1)

    # test if expand_most_upvote_comment fetch the most upvote command and invoke expand_branch with that comment id
    def test_expand_most_upvote_comment(self) -> None:
        #set up
        #create mock instance
        mock_client = Mock()
        #stub mock return
        mock_client.get_most_upvote_comment.return_value = [RedditServicer.construct_comment_from_dbrecord(self.mock_db.comment[0])]
        mock_client.expand_branch.return_value = [RedditServicer.construct_comment_from_dbrecord(self.mock_db.comment[4])]
        #function parameter
        post_id = 0

        #execution
        self.system_under_test.expand_most_upvote_comment(mock_client,post_id)

        #verify
        mock_client.get_most_upvote_comment.assert_called_with(post_id,1)
        mock_client.expand_branch.assert_called_with(self.mock_db.comment[0]['id'],5)

        #test if return_most_upvote_reply fetch the most upvote command, expand the list then return the most upvote reply
    def test_return_most_upvote_reply(self) -> None:
        #set up
        #create mock instance
        mock_client = Mock()
        #stub mock return
        mock_client.get_most_upvote_comment.return_value = [RedditServicer.construct_comment_from_dbrecord(self.mock_db.comment[0])]
        mock_client.expand_branch.return_value = [RedditServicer.construct_comment_from_dbrecord(self.mock_db.comment[4])]
        #function parameter
        post_id = 0

        #execution
        self.system_under_test.return_most_upvote_reply(mock_client,post_id)

        #verify
        mock_client.get_most_upvote_comment.assert_called_with(post_id,1)
        mock_client.expand_branch.assert_called_with(self.mock_db.comment[0]['id'],1)
        
if __name__ == '__main__':
    main()