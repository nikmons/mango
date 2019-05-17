import datetime

from app import db

from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, ForeignKey, String, Date, DateTime, Boolean, CheckConstraint

class Applicants(db.Model):
    __tablename__ = "Applicants"
    appl_id = Column('APPL_ID',Integer, primary_key=True)
    appl_created = Column('APPL_CREATED',DateTime, default=datetime.datetime.utcnow)
    appl_first_name = Column('APPL_FIRST_NAME',postgresql.VARCHAR(50))
    appl_middle_name = Column('APPL_MIDDLE_NAME',postgresql.VARCHAR(50), nullable=True)
    appl_last_name = Column('APPL_LAST_NAME',postgresql.VARCHAR(100))
    appl_father_name = Column('APPL_FATHER_NAME',postgresql.VARCHAR(50))
    appl_gender = Column('APPL_GENDER',postgresql.CHAR(1), CheckConstraint("APPL_GENDER in ('M', 'F')"))
    appl_date_of_birth = Column('APPL_DATE_OF_BIRTH',postgresql.DATE)
    appl_phone_num = Column('APPL_PHONE_NUM',postgresql.VARCHAR(10))
    appl_email = Column('APPL_EMAIL',postgresql.VARCHAR(100))
    appl_city = Column('APPL_CITY',postgresql.VARCHAR(100))
    country_ID = Column('COUNTRY_ID',Integer, ForeignKey('Countries.COUNTRY_ID'))
    appl_username = Column('APPL_USERNAME',postgresql.VARCHAR(100))
    appl_password = Column('APPL_PASSWORD',postgresql.VARCHAR(500)) # TODO: decide hash algo
    
    def __str__(self):
        return "<{}|{}:{}>".format(self.appl_id, self.appl_username, self.appl_email)

class Countries(db.Model):
    __tablename__ = 'Countries'
    country_id = Column('COUNTRY_ID', Integer, primary_key=True)
    country_iso_code = Column('COUNTRY_ISO_CODE', Integer)
    country_name = Column('COUNTRY_NAME', postgresql.VARCHAR(100))
    country_state_name = Column('COUNTRY_STATE_NAME', postgresql.VARCHAR(150))
    country_phone_code = Column('COUNTRY_PHONE_CODE', postgresql.VARCHAR(8))

    applicants = relationship('Applicants', backref='country')