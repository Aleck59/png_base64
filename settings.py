folder="png"
user_db="postgres"
pass_db="yourpass"
host_db="your.host"
port_db="5432"
db_name="your_table"

# table '''CREATE TABLE IF NOT EXISTS public.icon
# (
#     id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
#     name text COLLATE pg_catalog."default",
#     scale integer,
#     base64 text COLLATE pg_catalog."default",
#     CONSTRAINT "1" PRIMARY KEY (id)
#         INCLUDE(id)
# )'''