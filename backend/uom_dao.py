
def get_uom(connection1):
    cursor = connection1.cursor()
    query = "select * from uom"
    cursor.execute(query)
    response = []
    for (uom_id, uom_name) in cursor:
        response.append({
            'uom_id': uom_id,
            'uom_name': uom_name
        })
    return response


if __name__ == '__main__':
    from sql_connections import get_sql_connections

    connection = get_sql_connections()
    # print(get_all_products(connection))
    print(get_uom(connection))
