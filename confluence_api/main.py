from atlas.confluence import ConfluenceOperation
from atlas.confluence import Operation

import utils.environments as envs import utils.create_datas as dts
import utils.inquirers as inq


# Creamos la instancia
confluence = ConfluenceOperation(envs.get_url(), envs.get_user_email(), envs.get_token())

# Obtenemos espacios desde Confluence
spaces = confluence.get_spaces()

# Obtenemos la data que necesitamos || {"name": "name", "key": "key"}
spaces_prompt = dts.get_name_key_from_spaces(spaces)
# Obtenemos la lista de opciones a mostrar en el prompt 
choices = dts.get_choices_for_inquirer(spaces_prompt, dts.NAME)

# Mostramos las opciones y obtenemos la elegida
choice = inq.show_list(inq.create_inquirer_list(
    "Spaces",
    "Choose a space to perform an operation",
    choices
), "Spaces")

# Obtenemos el objeto con la opcion elegida, esto es necesario para,
# obtener la key y en base a esta traer todas las pages relacionadas
picked_space_dict = dts.get_obj_picked(dts.NAME, choice, spaces_prompt)

# Obtenemos las paginas
pages_from_space = {}
if picked_space_dict:
    pages_from_space = confluence.get_pages_from_space(picked_space_dict[dts.KEY])


# Obtenemos la data necesaria de los resultados de confluence
pages_prompt = dts.get_info_from_pages(pages_from_space)
# Creamos las opciones que daremos a elegir al usuario
choices_pages = dts.get_choices_for_inquirer(pages_prompt, dts.TITLE) 

# Mostramos las opciones y obtenemos la elegida
choice_page = inq.show_list(inq.create_inquirer_list(
    "Pages",
    "Choose a page to perform an operation",
    choices_pages,
), "Pages")

# Obtenemos el objeto con la opcion elegida, esto es necesario para,
# obtener la key y en base a esta traer todas las pages relacionadas
picked_page_dict = dts.get_obj_picked(dts.TITLE, choice_page, pages_prompt)

actions = [
    Operation.CREATE.name,
    Operation.UPDATE.name,
    Operation.DELETE.name,
]

action = inq.show_list(inq.create_inquirer_list(
    "Action",
    "Enter the operation you want to perform",
    actions,
), "Action")

operations = {
    Operation.CREATE.name: confluence.up_page(
        picked_space_dict[dts.KEY],
        "title",
        "body",
        #ParenId __ Page
    )
}

## Verificar de pasar a un archivo propio de markdown y paths

folders_choices = dts.get_folders_doc(envs.get_docs_path())

files = inq.show_list(inq.create_inquirer_list(
    "Files",
    "Select file to upload",
    dts.get_choices_for_inquirer(folders_choices, dts.NAME)
), "Files")

picked_selection = dts.get_obj_picked(dts.NAME, files, folders_choices)


if picked_selection is not None and dts.is_a_directory(picked_selection["path"]):
    folders_choices = dts.get_folders_doc(picked_selection["path"])

    files = inq.show_list(inq.create_inquirer_list(
        "Files",
        "Select file to upload",
        dts.get_choices_for_inquirer(folders_choices, dts.NAME)
    ), "Files")

    picked_selection = dts.get_obj_picked(dts.NAME, files, folders_choices)
    
else:    
    operations.get(action)
    
