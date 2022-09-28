import sqlite3


def load_date(sqlite_query: str, *args) -> list[tuple]:
    """ Возвращает запрашиваемое из базы данных """

    with sqlite3.connect("animal.db") as connection:
        cursor = connection.cursor()
        cursor.execute(sqlite_query, args)
        return cursor.fetchall()


def make_list_dict_format(keys: list[str], data: list[tuple]) -> list[dict]:
    """ Приводит данные к формату list[dict] """

    items = []

    for item_data in data:
        item = {}

        for i in range(len(item_data)):
            item[keys[i]] = item_data[i]

        items.append(item)

    return items


def make_list_format(data: list[tuple]) -> list:
    """ Приводит данные к формату list """

    new_data = []

    for part in data:
        part = list(part)
        new_data.extend(part)

    return new_data


def get_cat(item_id: int):
    """ Возвращает данные кота """

    query = """
            select cat_id, name, date_of_birth, age_upon_outcome, outcome_month_year
            from cats
            where id = ?
    """
    return load_date(query, item_id)


def get_cat_breed(cat_id: str) -> list[tuple]:
    """ Возвращает породу кота """

    query = """
        select breed
        from breeds
        where id in (select breed_id
			        from cat_breed 
			        where cat_id = ?)
    """
    return load_date(query, cat_id)


def get_cat_color(cat_id: str) -> list[tuple]:
    """ Возвращает цвет кота """

    query = """
        select color
        from colors
        where id in (select color_id
			        from cat_color 
			        where cat_id = ?)
    """
    return load_date(query, cat_id)


def get_outcome_type(item_id: int) -> list[tuple]:
    """ Что сейчас с котом """

    query = """
            select outcome_type
            from outcome_types
            where id = (select outcome_type_id
                        from cats
                        where id = ?)
    """

    return load_date(query, item_id)


def get_outcome_subtype(item_id: int) -> list[tuple]:
    """ В какой программе участвует кот """

    query = """
            select outcome_subtype
            from outcome_subtypes
            where id = (select outcome_subtype_id
                        from cats
                        where id = ?)
    """

    return load_date(query, item_id)


def get_item(item_id: int) -> dict:
    """ Возвращает все данные кота в словаре """

    cat = {}

    data = get_cat(item_id)
    keys = ['cat_id', 'name', 'date_of_birth', 'age_upon_outcome', 'outcome_year_month']
    cat.update(make_list_dict_format(keys, data)[0])

    data = get_cat_breed(cat['cat_id'])
    new_data = make_list_format(data)
    cat['breed'] = '/'.join(new_data)

    data = get_cat_color(cat['cat_id'])
    new_data = make_list_format(data)
    cat['color'] = ', '.join(new_data)

    data = get_outcome_type(item_id)
    if len(data) > 0:
        cat.update(make_list_dict_format(['outcome_type'], data)[0])

    data = get_outcome_subtype(item_id)
    if len(data) > 0:
        cat.update(make_list_dict_format(['outcome_subtype'], data)[0])

    return cat
