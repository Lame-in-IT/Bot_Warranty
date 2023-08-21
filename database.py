from tokin_bot import conect_bd
import psycopg2
import logging
 
def commect_bd():
    try:
        connection = psycopg2.connect(
            database=conect_bd["database"],
            user=conect_bd["user"],
            password=conect_bd["password"],
            host=conect_bd["host"],
            port=conect_bd["port"],
        )
        connection.autocommit = True
        return connection
    except Exception as ex:
        logging.exception(ex)
        
def read_bd(user_id):
    try:
        connection = commect_bd()
        list_id_user = []
        with connection.cursor() as cursor:
            cursor.execute("SELECT id_user FROM Bot_Warranty")
            list_id_user.extend(item_id_user[0] for item_id_user in cursor.fetchall())
        return str(user_id) in list_id_user
    except Exception as ex:
        logging.exception(ex)
        
def create_user(data_user):
    try:
        connection = commect_bd()
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO Bot_Warranty(id_user, is_bot, first_name, username, language_code)
                            VALUES(%s, %s, %s, %s, %s)""", [data_user["id"], data_user["is_bot"], data_user["first_name"],
                                                                    data_user["username"], data_user["language_code"]])
    except Exception as ex:
        logging.exception(ex)

def create_appeal_True(id_user, appeal_True):
    try:
        connection = commect_bd()
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE Bot_Warranty SET appeal_True = %s WHERE id_user = %s""", [
                        appeal_True, str(id_user)])
    except Exception as ex:
        logging.exception(ex)
        
def create_appeal(id_user, appeal):
    try:
        connection = commect_bd()
        list_appeal = []
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT appeal FROM Bot_Warranty WHERE id_user = '{id_user}'")
            for item_appeal in cursor.fetchall():
                list_appeal.extend(iter(item_appeal))
        list_appeal.append(str(appeal))
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE Bot_Warranty SET appeal = %s WHERE id_user = %s""", [
                        list_appeal, str(id_user)])
    except Exception as ex:
        logging.exception(ex)


def read_appeal_True(id_user):
    try:
        connection = commect_bd()
        list_appeal_True = []
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT appeal_True FROM Bot_Warranty WHERE id_user = '{id_user}'")
            list_appeal_True.extend(
                item_appeal_True[0] for item_appeal_True in cursor.fetchall()
            )
        return list_appeal_True[0]
    except Exception as ex:
        logging.exception(ex)



def create_screenshot(id_user, date):
    try:
        connection = commect_bd()
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE Bot_Warranty SET date = %s WHERE id_user = %s""", [
                        date, str(id_user)])
        return "Дата записана. Гарантия предоставлена."
    except Exception as ex:
        return "Дата не записана. произошла ошибка записи."

if __name__ == '__main__':
    commect_bd()