from sqlalchemy import(
    create_engine, table, column, Integer, String, MetaData
)

# Executing the instructions from our local host "rescueme" db
engine = create_engine("postgresql:///rescueme")

# Create a metadata instance
meta = MetaData()

# Create the users table
users_table = table(
    "users",
    column("id", Integer),
    column("name", String),
    column("age", Integer),
)

# Create a connection to the engine
with engine.connect() as connection:
    pass  # Add your code here