from sql_connections import get_sql_connections


def get_all_products(connection1):
    cursor = connection1.cursor()
    query = ("SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name "
             "FROM products inner join uom on products.uom_id=uom.uom_id")
    cursor.execute(query)
    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append(
            {
                'product_id': product_id,
                'name': name,
                'uom_id': uom_id,
                'price_per_unit': price_per_unit,
                'uom_name': uom_name
            }
        )

    return response


def insert_new_product(connection2, product):
    cursor = connection2.cursor()
    query = ("insert into products"
             "(name, uom_id, price_per_unit)"
             "values (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection2.commit()
    return cursor.lastrowid


def delete_product(connection3, product_id):
    cursor = connection3.cursor()
    query = ("delete from products where product_id=" + str(product_id))
    cursor.execute(query)
    connection3.commit()


if __name__ == '__main__':

    connection = get_sql_connections()
    print(delete_product(connection, 9))
