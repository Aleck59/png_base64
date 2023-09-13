import os
import base64
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import settings
def main():
    fol = os.getcwd()+f"\{settings.folder}"
    namesonly= [f for f in os.listdir(fol) if f.endswith('.png') or f.endswith('.ico') or f.endswith('.gif')]
    connection = psycopg2.connect(user=settings.user_db,
                                  password=settings.pass_db,
                                  host=settings.host_db,
                                  port=settings.port_db,
                                  database=settings.db_name)
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    for i, file in enumerate(namesonly):
        contents = open(os.path.join(fol, file), 'rb').read()
        encoded = base64.b64encode(contents)
        cursor.execute(f"""Insert into icon (name , base64) values('{file}','{encoded.decode('utf-8')}')""")
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


