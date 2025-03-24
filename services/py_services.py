from connection import py_connection


def fn_services_management(request):
    rval = 0
    msg = "Something went wrong!"
    services = []
    try:
        action = request.get("action", "")
        service_id = request.get("service_id")
        service_name = request.get("service_name")
        service_description = request.get("service_description")
        if action == "update":
            sqry = f'''UPDATE services SET service_name = '{service_name}',
                    service_description = '{service_description}' WHERE service_id = '{service_id}'; '''
            print(sqry)
            res = py_connection.do_result(sqry)
            if res:
                rval = 1
                msg = "Updated Successfully! "
        qry = "select service_id, service_name, service_description from services where 1=1 "
        result, key = py_connection.get_result_col(qry)
        print(result)
        if result:
            rval = 1
            msg = "success"
            for row in result:
                data = dict(zip(key, row))
                services.append(data)
        return {"rval": rval, "msg": msg, "services": services}
    except Exception as e:
        print("Exception in fn_services_management " + str(e))
        return {"rval": rval, "msg": msg, "services": services}


def fn_user_management(request):
    rval = 0
    msg = "Something went wrong!"
    users = []
    try:
        action = request.get("action", "")
        user_id = request.get("user_id")
        if action == "delete" and user_id:
            sqry = f'''DELETE FROM Users WHERE user_id = {user_id}; '''
            print(sqry)
            py_connection.do_result(sqry)
        qry = "select user_id, username from users where 1=1 "
        result, key = py_connection.get_result(qry)
        print(result)
        if result:
            rval = 1
            msg = "success"
            for row in result:
                data = dict(zip(key, row))
                users.append(data)
        return {"rval": rval, "msg": msg, "users": users}
    except Exception as e:
        print("Exception in fn_user_management " + str(e))
        return {"rval": rval, "msg": msg, "users": users}


def fn_notes(request):
    rval = 0
    msg = "Something went wrong!"
    notes = []
    try:
        # request_d = json.loads(data)
        content = request.get("note")
        user_id = request.get("user_id")
        action = request.get("action", "")
        fetch_query = f"select content from Notepad where user_id = {user_id} "
        result, key = py_connection.get_result(fetch_query)
        print(result)
        if result:
            rval = 1
            msg = "success"
            for row in result:
                data = dict(zip(key, row))
                notes.append(data)
        if action == "update":
            update_qry = f"update Notepad set content = {content} where user_id = {user_id}"
            updated_res = py_connection.do_result(update_qry)
            if updated_res:
                res, keys = py_connection.get_result(fetch_query)
                if res:
                    notes = [dict(zip(keys, row)) for row in result]
                    print(res)
                    if res:
                        rval = 1
                        msg = "updated successfully"
        return {"rval": rval, "msg": msg, "notes": notes}
    except Exception as e:
        print("Exception in fn_notes " + str(e))
        return {"rval": rval, "msg": msg, "notes": notes}
