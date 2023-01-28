from fastapi import HTTPException
from http import HTTPStatus


def check_table_for_values(
    table_rows: int,
    table_columns: int,
    rows: int,
    columns: int
):
    if table_rows > rows:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Количество добавляемых строк больше чем строк таблицы'
        )
    if table_columns > columns:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Количество добавляемых колонок больше чем колонок таблицы'
        )
