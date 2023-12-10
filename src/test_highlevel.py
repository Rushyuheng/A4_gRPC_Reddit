from client import RedditClient
from highlevel import HighLevel
from unittest import TestCase, main
from unittest.mock import patch, Mock
from mock_db import MockDB

class TestHighLevel(TestCase):
    def setUp(self) -> None:
        self.system_under_test = HighLevel()
        self.mock_db = MockDB()

        # test if retrieve invoke correct client function with correct parameter
    def test_retrieve_post(self) -> None:
        #set up
        #create mock instance
        mock_client = Mock()
        #stub mock return
        mock_client.get_post.return_value = self.mock_db.post[0]

        #function parameter
        post_id = 0

        #execution
        self.system_under_test.retrieve_post(mock_client,post_id)

        #verify
        mock_client.get_post.assert_called_with(post_id)


if __name__ == '__main__':
    main()