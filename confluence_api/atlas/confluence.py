from atlassian import Confluence
from enum import Enum

    
def singleton(cls):

    instances = dict()

    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)

        return instances[cls]

    return wrap


class Operation(Enum):
    CREATE = 1
    UPDATE = 2
    DELETE = 3
    

@singleton
class ConfluenceOperation():

    confluence : None
    
    
    def __init__(self, url, username, password):
        self.confluence = Confluence(
            url=url,
            username=username,
            password=password
        )


    def get_spaces(self):
        return self.confluence.get_all_spaces()

    
    def get_pages_from_space(self, key):
        return self.confluence.get_all_pages_from_space(key)


    def up_page(self, space, title, body, parent_id=None):
        self.confluence.create_page(space, title, body, parent_id)

