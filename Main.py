from argparse import ArgumentParser
from command_tool.NewPost import *
from command_tool.Past75 import *
from command_tool.VoteCount import *

class Main:

    def __init__(self):
        self.__new_url = ''

    """ 
    Retrieves the newest reddit posts.
    Params:
        url: String representing an api request.
    """
    def run_new(self, url):
        new_post = NewPost(url)
        new_post.extract()
        new_post.update_url()
        self.__new_url = new_post.get_url()
        
        if new_post._get_response()['data']['dist'] == 0:
            return 'No more new posts!'

    """ Retrieve reddit posts not in the top 75 posts. 
    Params:
        url: String representing an api request.
    """ 
    def run_past_75(self, url):
        past_75 = Past75(url)
        past_75.update_url()
        past_75.extract()
    
    """ Retrieves the vote count on reddit posts. 
    Params:
        url: String representing an api request.
    """ 
    def run_vote_count(self, url):
        vote_count = VoteCount(url)
        vote_count._get_upvote()
    
    """ Getter for updated url. """
    def get_new_url(self):
        return self.__new_url
    
    def run(self):
        print("Enter the number that corresponds to which Reddit data you'd like to view:\n \
            1. New Posts\n \
            2. Posts No longer in the top 75\n \
            3. Posts with a vote count change.\n")
        command = input('Enter a command: ')

        # parse user command to trigger desired post type.
        if command == '1':
            new_listing = main.run_new('https://www.reddit.com/r/oddlysatisfying/new.json')

            running = True
            while running:
                user_response = str(input('Would you like to see the latest new posts again? Enter yes/no: ')).lower()
                if (user_response == 'yes') and (new_listing != 'No more new posts!'):
                    main.run_new(main.get_new_url())
                elif user_response == 'no':
                    running = False
                elif new_listing == 'No more new posts!':
                    print('No more new posts!')
                    running = False
        elif command == '2':
            main.run_past_75('https://www.reddit.com/r/oddlysatisfying/top.json')
        elif command == '3':
            main.run_vote_count('https://www.reddit.com/r/oddlysatisfying/top.json')
        else:
            print('Invalid input. Try again!\n\n')
            self.run()


if __name__ == "__main__":
    main = Main()
    main.run()