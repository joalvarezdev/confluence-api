from atlas.confluence import Operation

import inquirer
import utils.create_datas as dts


def validate_not_empty(answers, current):
    if not current.strip():
        raise inquirer.errors.ValidationError("", reason="You must enter a value")
    return True


def create_inquirer_list(id, _message, _choices):
    return [
        inquirer.List(
            id,
            message=_message,
            choices=_choices,
        )
    ]


def show_list(list_inquirer, id):
    return inquirer.prompt(
        list_inquirer
    )[id]


def show_list_text(list_text):
    return inquirer.prompt(
        list_text
    )

def create_crud_operations(list_text):
    inqs = []
    for element in list_text:
        if "key" in element and "content" in element:
            inqs.append(
                inquirer.Text(
                    element["key"],
                    message=element["content"],
                    validate=validate_not_empty if element["validate"] else None,
                )
            )
    return inqs 


def test_text():
    questions = [
        inquirer.Text(
            "name",
            message="Ingrese titulo de la pagina",
            validate=validate_not_empty,
        ),
        inquirer.Text(
            "path",
            message="Ingrese el path del contenido a subir",
            validate=validate_not_empty,
        ),
    ]

    return inquirer.prompt(questions)


# def create_questions(data):
#     inqs = []
#     for element in data:
#         inqs.append(
#             inquirer.Text(
#                 element[dts.KEY],
#                 message=element[dts.MESSAGE]
#                 validate=validate_not_empty,
#             ))
#     return inqs
