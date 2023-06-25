import utils.environments as envs
import os

RESULTS = "results"
KEY = "key"
NAME = "name"

TITLE = "title"
ID = "id"

MESSAGE="message"

def get_name_key_from_spaces(spaces):
    if spaces is not None and RESULTS in spaces:
        data = []
        for element in spaces[RESULTS]:
            space = {}
            space[NAME] = element[NAME]
            space[KEY] = element[KEY]
            data.append(space)
        return data


def get_choices_for_inquirer(listObjects, property):
    if listObjects is not None:
        choices = []
        for element in listObjects:
            choices.append(element[property])
        choices.append("NONE")
        return choices


def get_obj_picked(key, choice, listObjects):
    for obj in listObjects:
        if obj[key] == choice:
            return obj


def get_info_from_pages(pages):
    if pages is not None:
        pages_formats = []
        for element in pages:
            data = {}
            data[ID] = element[ID]
            data[TITLE] = element[TITLE]
            pages_formats.append(data)

        return pages_formats


def is_a_directory(path):
    return os.path.isdir(path)

def get_folders_doc(docs):
    folders = [] 
    # docs = envs.get_docs_path()
    
    # if select:
    #     docs = f"{docs}/{select}"
    
    for element in os.listdir(docs):
        data = {}
        #paths = os.path.join(str(docs), element)
            
        data["path"] = f"{docs}/{element}"
        data["name"] = element
        folders.append(data)
    return folders


