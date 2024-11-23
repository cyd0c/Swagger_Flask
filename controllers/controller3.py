from flask import request, jsonify



def todos_get() -> str:

    return 'do some magic!', 200

def todos_id_delete(id) -> str:
    return 'do some magic!'

def todos_id_get(id) -> str:
    return 'do some magic!'

def todos_id_put(id, body) -> str:
    return 'do some magic!'

def todos_post(body) -> str:
    return 'do some magic!'
