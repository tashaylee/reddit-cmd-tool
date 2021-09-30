from command_tool.NewPost import NewPost

""" This class represents posts that are no longer on the top 75 reddit posts. """
class Past75(NewPost):

    def __init__(self, url):
        super().__init__(url)

    """ Gets the last post's id from entire listing. """
    def _get_last_child(self):
        list_of_posts = self._getChildren(self._response)
        child = list_of_posts[len(list_of_posts) - 1]
        post_id = child['data']['name']
        return post_id
    
    """ Adds params to the api request url to point to the post after the 75th post. """
    def update_url(self):
        self.set_url(self.get_url() + '?count=75&after=' + self._get_last_child())


if __name__ == '__main__':
    past_75 = Past75('https://www.reddit.com/r/oddlysatisfying/top.json')
    past_75.extract()
    past_75_2 = Past75('https://www.reddit.com/r/oddlysatisfying/top.json')
    past_75_2.extract()

    # testing if id corresponds to a post link.
    assert 't3_' in past_75._get_last_child(), 'successfully retrieved a post reference!'

    # testing if url updates to get url before most recent post.
    past_75.update_url()
    assert past_75.get_url() == 'https://www.reddit.com/r/oddlysatisfying/top.json?limit=25&before=' \
        + past_75._get_last_child(), 'url matches and is updated!'

    # testing if id corresponds to a post link.
    assert 't3_' in past_75_2._get_last_child(), 'successfully retrieved a post reference!'

    # testing if url updates to get url before most recent post.
    past_75_2.update_url()
    assert past_75_2.get_url() == 'https://www.reddit.com/r/oddlysatisfying/top.json?limit=25&before=' \
        + past_75_2._get_last_child(), 'url matches and is updated!'