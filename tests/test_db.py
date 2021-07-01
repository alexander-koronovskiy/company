from handler_db import sql_query


def test_count_unique_values():
    """Подсчет уникальных значений"""
    assert sql_query("SELECT COUNT(DISTINCT first_name) FROM user")


def test_unique_values():
    """Вывод списка уникальных значений"""
    assert sql_query(
        """
    SELECT first_name,COUNT(first_name)
    FROM user
    GROUP BY first_name
    """
    )


def test_sort_columns():
    """Сортирвка значений с условием
    в порядке возрастания / в порядке убывания"""
    assert sql_query(
        """
    SELECT * FROM user
    WHERE state='Iran'
    ORDER BY first_name ASC
    """
    )
    assert sql_query(
        """
    SELECT * FROM user
    WHERE state='Iran'
    ORDER BY first_name DESC
    """
    )


def test_insertion():
    """вставка значений в базу данных"""
    assert not sql_query(
        """
        INSERT INTO user (first_name, last_name, gender, phone, email, state, img)
        VALUES ('alex', 'leo', 'male', '7 800 961 54 41', 'alex_leo@gmail.com', 'USA', '46.png')
        """
    )
