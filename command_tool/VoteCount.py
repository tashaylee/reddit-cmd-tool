from command_tool.RedditPost import _RedditPost

""" This class represents reddit posts with a change in upvote counts. """
class VoteCount(_RedditPost):

    def __init__(self, url):
        super().__init__(url)

    """ Makes an api request that gets the number of upvotes. """
    def _get_upvote(self):
        initial_listing = self._getChildren(self._response) # references initial response's reddit listing.
        secondary_listing = self.__get_secondary_listing() # references secondary response's reddit listing.

        # get upvote count for every post.
        for post in range(len(initial_listing) - 1):
            initial_post = initial_listing[post]['data']['name']
            secondary_post = secondary_listing[post]['data']['name']

            initial_upvote = initial_listing[post]['data']['ups']
            secondary_upvote = secondary_listing[post]['data']['ups']

            # check if there's a change in secondary listing's and initial listing's upvotes.
            if (initial_post == secondary_post) and (initial_upvote != secondary_upvote): # check if referencing same post
                count_change = abs(initial_upvote - secondary_upvote)
                print('Title: \t' + self._get_title(initial_listing, post))
                print('Author: \t' + self._get_author(initial_listing, post))
                print('Permalink: \t' + self._get_permalink(initial_listing, post))
                print("Initial Upvote Count:\t" + str(initial_upvote))
                print("Secondary Upvote Count:\t" + str(secondary_upvote))
                print("Upvote Count Change:\t" + str(count_change) + "\n")
    
    """
    Creates secondary api request.

    Returns:
        A list of individual reddit posts from secondary response.
    """
    def __get_secondary_listing(self):
        secondary_response = self._get_response()
        return self._getChildren(secondary_response)


if __name__ == '__main__':
    vote_count = VoteCount('https://www.reddit.com/r/oddlysatisfying/top.json')
    vote_count.extract()
    vote_count._get_upvote()