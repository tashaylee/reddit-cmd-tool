import json
import requests

""" This class represents all RedditPosts """
class _RedditPost:
    
    def __init__(self, url):
        self.__url = url
        self._response = self._get_response()

    """ 
    Sends a request to reddit api.

    Returns:
        A json response.
    """
    def _get_response(self):
        response = requests.get(self.__url, headers = {'User-agent': 'Bot 1.0'})
        return response.json()

    """ 
    Gets all reddit posts within a reddit listing.
    
    Params:
        response: A JSON response.
    Returns:
        A list of individual reddit posts.
    """
    def _getChildren(self, response):
        return response["data"]["children"]

    """ 
    Sets the title, author, url from a reddit post.
    
    Params:
        listing: A list of individual reddit posts.
        post: A dictionary containing information that represents a single reddit post.
    """
    def _get_title(self, listing, post):
        return listing[post]['data']['title']

    def _get_author(self, listing, post):
        return listing[post]['data']['author']
    
    def _get_permalink(self, listing, post):
        return 'https://www.reddit.com' + listing[post]['data']['permalink']

    """ 
    Gets all information from a list of reddit posts.

    Params:
        listing: A list of individual reddit posts.
    """
    def _get_info(self, listing):
        for post in range(len(listing)-1):
            print("Title:\t" + self._get_title(listing, post))
            print("Author:\t" + self._get_author(listing, post))
            print("URL:\t" + self._get_permalink(listing, post)+ '\n')


    """ 
    Setter for the reddit api url.

    Params:
        url: String representing an api request.
    """
    def set_url(self, url):
        self.__url = url
    
    """
    Gets the reddit api url .

    Returns:
        String representing an api request.
    """
    def get_url(self):
        return self.__url

    """ Extracts reddit post information. """
    def extract(self):
        listing = self._getChildren(self._get_response())
        self._get_info(listing)


if __name__ == '__main__':
    post = _RedditPost('https://www.reddit.com/r/oddlysatisfying.json')
    post.extract()