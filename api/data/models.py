from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import List


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=False)
    email:Mapped[str] = mapped_column(nullable=False)
    password:Mapped[str] = mapped_column(nullable=False)
    role:Mapped[str] = mapped_column(nullable=False)
    university_id:Mapped[int] = mapped_column(nullable=False)
    university:Mapped["University"] = relationship(back_populates="users")
    programs:Mapped[list["Program"]] = relationship(back_populates="user")
    courses:Mapped[list["Course"]] = relationship(back_populates="user")
    students:Mapped[list["Student"]] = relationship(back_populates="user")
    instructors:Mapped[list["Instructor"]] = relationship(back_populates="user")
    topics:Mapped[list["Topic"]] = relationship(back_populates="user")
    #posts:Mapped[list["Post"]] = relationship(back_populates="user")
    #comments:Mapped[list["Comment"]] = relationship(back_populates="user")

class University(Base):
    __tablename__ = 'universities'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=False)
    programs:Mapped[list["Program"]] = relationship(back_populates="university")

class Program(Base):
    __tablename__ = 'programs'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=False)
    university_id:Mapped[int] = mapped_column(nullable=False)
    university:Mapped["University"] = relationship(back_populates="programs")
    courses:Mapped[list["Course"]] = relationship(back_populates="program")

class Course(Base):
    __tablename__ = 'courses'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=False)
    program_id:Mapped[int] = mapped_column(nullable=False)
    program:Mapped["Program"] = relationship(back_populates="courses")
    students:Mapped[list["Student"]] = relationship(back_populates="course")
    instructors:Mapped[list["Instructor"]] = relationship(back_populates="course")

class Student(Base):
    __tablename__ = 'students'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=False)
    course_id:Mapped[int] = mapped_column(nullable=False)
    course:Mapped["Course"] = relationship(back_populates="students")

class Instructor(Base):
    __tablename__ = 'instructors'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=False)
    course_id:Mapped[int] = mapped_column(nullable=False)
    course:Mapped["Course"] = relationship(back_populates="instructors")        

class Topic(Base):
    __tablename__ = 'topics'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=False)
    course_id:Mapped[int] = mapped_column(nullable=False)
    course:Mapped["Course"] = relationship(back_populates="topics")

class Quiz(Base):
    __tablename__ = 'quizzes'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=False)
    course_id:Mapped[int] = mapped_column(nullable=False)
    course:Mapped["Course"] = relationship(back_populates="quizzes")

class Question(Base):
    __tablename__ = 'questions'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=False)
    quiz_id:Mapped[int] = mapped_column(nullable=False)
    quiz:Mapped["Quiz"] = relationship(back_populates="questions")
    topic_id:Mapped[int] = mapped_column(nullable=False)   

class QuizQuestion(Base):
    __tablename__ = 'quiz_questions'
    id:Mapped[int] = mapped_column(primary_key=True)
    question_id:Mapped[int] = mapped_column(nullable=False)
    quiz_id:Mapped[int] = mapped_column(nullable=False)
    quiz:Mapped["Quiz"] = relationship(back_populates="quiz_questions")
    question:Mapped["Question"] = relationship(back_populates="quiz_questions")    
