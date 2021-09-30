from command_tool.RedditPost import _RedditPost

""" This class represents new reddit posts. """
class NewPost(_RedditPost):

    def __init__(self, url):
        super().__init__(url)
        self.__last_post = dict()


    """ Gets the most recent post's id from listing. """
    def _get_recent_child(self):
        list_of_posts = self._getChildren(self._response)
        child = list_of_posts[0]
        post_id = child['data']['name']
        return post_id
    
    """ Adds params to the request to point to the most recent reddit post. """
    def update_url(self):
        self.set_url(self.get_url() + '?limit=25&before=' + self._get_recent_child())

        
if __name__ == '__main__':
    new_post = NewPost('https://www.reddit.com/r/oddlysatisfying/new.json')
    new_post.extract()
    new_post2 = NewPost('https://www.reddit.com/new.json')
    new_post2.extract()

    # testing if id corresponds to a post link.
    assert 't3_' in new_post._get_recent_child(), 'successfully retrieved a post reference!'

    # testing if url updates to get url before most recent post.
    new_post.update_url()
    assert new_post.get_url() == 'https://www.reddit.com/r/oddlysatisfying/new.json?limit=25&before=' \
        + new_post._get_recent_child(), 'url matches and is updated!'

    # testing if id corresponds to a post link.
    assert 't3_' in new_post2._get_recent_child(), 'successfully retrieved a post reference!'

    # testing if url updates to get url before most recent post.
    new_post2.update_url()
    assert new_post2.get_url() == 'https://www.reddit.com/new.json?limit=25&before=' \
        + new_post2._get_recent_child(), 'url matches and is updated!'