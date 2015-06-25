from sqlalchemy import Table, MetaData, Column, String, Integer, Text, create_engine
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///dev.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(Text)

    def __repr__(self):
        return self.title

class PostRepo(object):

    def __init__(self):
        self.session = Session()

    def all(self):
        return self.session.query(Post).all()

    def create(self, title, body):
        post = Post(title=title, body=body)
        self.session.add(post)
        self.session.commit()
        return post

    def find(self, id):
        return self.session.query(Post).filter(Post.id == id).first()

    def update(self, post):
        self.session.add(post)
        self.session.commit()

    def delete(self, post):
        self.session.delete(post)
        self.session.commit()


Base.metadata.create_all(engine)
