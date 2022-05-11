from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

eng = create_engine('sqlite:///ica06.sqlite')

Base = declarative_base()

class Book(Base):
    __tablename__ = "Book"

    Id = Column(Integer, primary_key=True)
    Author = Column(String)
    Name = Column(String)

books = [Book(Id=1, Author="Mark Twain", Name="The Adventures of Tom Sawyer"),
    Book(Id=2, Author="Charles Dickens", Name="David Copperfield"),
    Book(Id=3, Author="Jules Verne", Name="20,000 Leagues Under the Sea"),
    Book(Id=4, Author="Lewis Carroll", Name="Alice’s Adventures in Wonderland"),
    Book(Id=5, Author="James Joyce", Name="Ulysses"),
    Book(Id=6, Author="F. Scott Fitzgerald", Name="The Great Gatsby"),
    Book(Id=7, Author="James Joyce", Name="Ulysses")]

Base.metadata.bind = eng
Base.metadata.create_all()

Session = sessionmaker(bind=eng)
ses = Session()

# Clear any existing data from Book table so we can insert fresh data
ses.query(Book).delete()
ses.commit()

ses.add_all(books)
ses.commit()

rs = ses.query(Book).all()
for book in rs:
    print("Author: {} * Book: {}".format(book.Author, book.Name))