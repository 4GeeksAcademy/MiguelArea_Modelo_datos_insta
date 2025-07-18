from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(50))
    lastname: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    bio: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    created_at: Mapped[str] = mapped_column(String(20))


    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "bio": self.bio,
            "created_at": self.created_at
        }
    
class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'), nullable=False)
    content: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[str] = mapped_column(String(20))
    likes: Mapped[int] = mapped_column()

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "content": self.content,
            "created_at": self.created_at,
            "likes": self.likes
        }
    
class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'), nullable=False)
    post_id: Mapped[int] = mapped_column(db.ForeignKey('post.id'), nullable=False)
    created_at: Mapped[str] = mapped_column(String(20))

    def serialize(self):
        return {
            "id": self.id,
            "comment_text": self.comment_text,
            "user_id": self.user_id,
            "post_id": self.post_id,
            "created_at": self.created_at
        }
    
class Media(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(10))  # image, video, audio, text
    url: Mapped[str] = mapped_column(String(255))
    post_id: Mapped[int] = mapped_column(db.ForeignKey('post.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "url": self.url,
            "post_id": self.post_id
        }
    
class Follower(db.Model):
    user_from_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'), primary_key=True)
    user_to_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'), primary_key=True)

    def serialize(self):
        return {
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id
        }