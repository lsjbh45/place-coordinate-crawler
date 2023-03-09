from dotenv import load_dotenv
import os
from lib.db import Database
from lib.kakao_api import KakaoApi
from lib.logger import Logger


def get_env():
    load_dotenv()

    host = os.environ.get('HOST')
    port = os.environ.get('PORT')
    user = os.environ.get('USER')
    password = os.environ.get('PASSWORD')
    database = os.environ.get('DATABASE')

    token = os.environ.get('TOKEN')

    table = os.environ.get('TABLE')
    pk_col = os.environ.get('PK_COL')
    address_col = os.environ.get('ADDRESS_COL')
    latitude_col = os.environ.get('LATITUDE_COL')
    longitude_col = os.environ.get('LONGITUDE_COL')

    return \
        host, port, user, password, database, token, \
        table, pk_col, address_col, latitude_col, longitude_col


if __name__ == "__main__":
    host, port, user, password, database, token, \
        table, pk_col, address_col, latitude_col, longitude_col = get_env()

    database = Database(host, port, user, password, database)
    kakao_api = KakaoApi(token)
    logger = Logger()

    select = database.fetchall(f'''
        SELECT "{pk_col}", "{address_col}"
          FROM "{table}"
         WHERE "{latitude_col}"  IS NULL
            OR "{longitude_col}" IS NULL
    ''')

    count = 0
    for pk, address in select:
        x, y = kakao_api.find_coordinate(address)
        if not x or not y:
            logger.info(f'failed: {pk}, {address}')
            continue

        database.execute(f'''
            UPDATE "{table}"
               SET "{latitude_col}"  = {y},
                   "{longitude_col}" = {x}
             WHERE "{pk_col} = {pk}
        ''')
        count += 1

    database.commit()
    logger.info(f'success: {count}')
