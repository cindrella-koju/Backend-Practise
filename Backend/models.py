from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, Session
from typing import Optional
from sqlalchemy import String, select

DB_URL = "postgresql+psycopg2://cindrella:postgres@localhost:5432/test"
engine = create_engine(DB_URL,echo=True)

if not database_exists(engine.url):
    create_database(engine.url)
    print(f"Database '{engine.url.database}' created.")
else:
    print(f"Database '{engine.url.database}' already exists.")

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"

    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(30))
    full_name : Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.full_name!r})"
    
# Base.metadata.create_all(engine)

# with Session(engine) as session:
#     spongebob = User(name = "SpongeBob", full_name = "Spongebob Squarepants")
#     session.add(spongebob)
#     session.commit()

session = Session(engine)

stmt = select(User)
print(session.scalar(stmt))
