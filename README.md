# folktales

`folktales` enables the creation, access and modification of SQL databases, with an emphasis on storing dictionaries easily and accessing database tables as pandas DataFrames easily. It also provides template dictionaries suitable for logging. While it can be used with other databases, it is designed currently to be used easily with SQLite3 databases.

`folktales` might be used in a logging context, whereby a status dictionary, which features a UUID4 identifier and a UTC datetime by default, is updated with program characteristics or other data and then saved to database.

# setup

```Bash
pip install folktales
```

`Sqliteman` is a GUI tool that can be used to interact with SQLite3 databases.

```Bash
apt install sqliteman
```

# examples

## create a database

```Python
folktales.create_database(filepath = "database.db")
```

## access a database

```Python
database = folktales.access_database(filepath = "database.db")
```

## insert a dictionary into a database table

```Python
folktales.insert_dictionary_into_database_table(
    dictionary      = {
                      "a": 1,
                      "b": 2
                      },
    table_name      = "data",
    filepath        = "database.db"
)
```

## state dictionaries

A template state dictionary can be created in the following way:

```Python
folktales.template_state_dictionary()
```

This returns a dictionary that features a UUID4 identifier (`uuid.uuid4()`) and a datetime (`datetime.datetime.utcnow()`).

A state dictionary can be created at the same time as updating it with an existing dictionary in the following way:

```Python
folktales.state_dictionary(
    entries = {
              "state_ID"             : "84f80687-cdd7-48f9-b21c-3d75fd759604",
              "price_recommendation" : 5007.24
              }
)
```

## insert a state dictionary into a database table

```Python
folktales.insert_state_dictionary_into_database_table(
    entries    = {
                 "state_ID"             : "84f80687-cdd7-48f9-b21c-3d75fd759604",
                 "price_recommendation" : 5007.24
                 },
    table_name = "do_stocks",
    filepath   = "database.db"
)
```

## access a database table as a pandas DataFrame

```Python
df = folktales.DataFrame_of_database_table(
    filepath   = "database.db",
    table_name = "do_stocks"
)
```
