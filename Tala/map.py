from typing import Literal
from dataentry import add_row, get_data, get_row, save_data, set_cell

# simplified dataentry api for answering questions and data

Done = Literal[0,1]

def initdata(data, user):
    user = int(user)
    table = get_data(data)
    try:
        print('Getting row')
        row = get_row(table,user)
    except KeyError:
        print('KeyError! Adding row')
        row = add_row(table,user)
    return table,row

def edit(data, user,name,value:Done):
    # Student usernames are numeric ids; the admin login ("Admin") is not a
    # tracked learner, so skip the progress write instead of crashing on int().
    try:
        user = int(user)
    except (TypeError, ValueError):
        return
    table,row = initdata(data, user)
    set_cell(table,user,name,value)
    save_data(data,table)

def done_module(data, user,name):
    edit(data, user,'m_'+name,1)

def set_question(data, user,name,right:Done):
    edit(data, user,'q_'+name,right)


