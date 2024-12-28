import mysql.connector


def is_user_created(db_config, username):

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    query = "SELECT COUNT(*) FROM user WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result[0] > 0


def is_user_deleted(db_config, username):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    query = "SELECT COUNT(*) FROM user WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result[0] == 0