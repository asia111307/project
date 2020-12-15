from sqlalchemy.types import String, Integer
from sqlalchemy import Column, ForeignKey, DateTime
import os, shutil
from start import db, app
import datetime


class Event(db.Model):
    __tablename__ = 'event'
    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String, default='')
    thumbnail = Column(String, default='')
    start_date = Column(DateTime, default=datetime.datetime.now())
    end_date = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, title, thumbnail, start_date, end_date):
        self.title = title
        self.thumbnail = thumbnail
        self.start_date = start_date
        self.end_date = end_date

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'thumbnail': self.thumbnail,
            'start_date': self.start_date,
            'end_date': self.end_date,
        }

    @staticmethod
    def get_all_events():
        """ Returns list of events """
        return Event.query.all()


class Registration(db.Model):
    __tablename__ = 'registration'
    id = Column(Integer, autoincrement=True, primary_key=True)
    event_id = Column(Integer, ForeignKey('event.id'))
    fullname = Column(String, default='')
    manage_code = Column(String, default='')
    creation_date = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, event_id, fullname, manage_code):
        self.event_id = event_id
        self.fullname = fullname
        self.manage_code = manage_code

    def to_json(self):
        return {
            'id': self.id,
            'event_id': self.event_id,
            'fullname': self.fullname,
            'manage_code': self.manage_code,
            'creation_date': self.creation_date,
        }

    @staticmethod
    def get_all_registrations():
        """ Returns list of registrations """
        return Registration.query.all()


def initiate_db_with_data():
    """ Prepares first event and reservation """

    events = Event.query.all()
    if not events:
        db.session.add(Event('IT webinar', 'thumbnails/e3.jpeg',  datetime.datetime.now(), datetime.datetime.now()))
        db.session.add(Event('SEO foundations', 'thumbnails/e4.jpeg', datetime.datetime.now(), datetime.datetime.now()))
        db.session.add(Event('How to be a happy dad', 'thumbnails/e2.jpeg', datetime.datetime.now(), datetime.datetime.now()))
        db.session.commit()

    first_registration = Registration.query.all()
    if not first_registration:
        db.session.add(Registration(1, 'John Doe', 'abc123xyz'))
        db.session.commit()


