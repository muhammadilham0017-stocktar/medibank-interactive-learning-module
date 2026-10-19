from typing import Literal
from dataentry import add_row, get_data, get_row, save_data, set_cell

# simplified dataentry api for answering questions and data

Done = Literal[0,1]

# The demo logins use friendly names, but the progress tracker is keyed by a
# numeric student id. Map the student login to its id; the admin login is not a
# tracked learner, so it is skipped (see _as_id returning None).
_DEMO_IDS = {"student": 12345678}

def _as_id(user):
    """Numeric tracking id for a login, or None when it should not be tracked."""
    if isinstance(user, str):
        mapped = _DEMO_IDS.get(user.strip().lower())
        if mapped is not None:
            return mapped
    try:
        return int(user)
    except (TypeError, ValueError):
        return None

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
    uid = _as_id(user)
    if uid is None:          # e.g. the admin login — not a tracked learner
        return
    table,row = initdata(data, uid)
    set_cell(table,uid,name,value)
    save_data(data,table)

def done_module(data, user,name):
    edit(data, user,'m_'+name,1)

def set_question(data, user,name,right:Done):
    edit(data, user,'q_'+name,right)


