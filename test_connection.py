from app.database import engine
from sqlalchemy import text

with engine.connect() as connection:
    result = connection.execute(
        text("select * from current_database()")
    )
    print("Connected to:", result.scalar_one())
