"""
    Nay Oo Kyaw
    nayookyaw.nok@gmail.com
"""

from __main__ import db

class Sensor(db.Model):
  """ Data model for sensor """

  __tablename__ = 'sensors'
  
  id = db.Column(
    db.Integer,
    primary_key = True
  )
  sensor_name = db.Column(
    db.String(150),
    index = True,
    unique = False,
    nullable= True
  )
  mac_address = db.Column(
    db.String(150),
    index = False,
    unique = False,
    nullable = True
  )
  room = db.Column(
    db.String(250),
    index = False,
    unique = False,
    nullable = True
  )
  floor = db.Column(
    db.String(250),
    index = False,
    unique = False,
    nullable = True
  )
  building = db.Column(
    db.String(250),
    index = False,
    unique = False,
    nullable = True
  )
  location = db.Column(
    db.String(250),
    index = False,
    unique = False,
    nullable = True
  )
  is_block = db.Column(
    db.String(150),
    index = False,
    unique = False,
    nullable = True
  )
  updated_at = db.Column(
    db.DateTime,
    index = False,
    unique = False,
    nullable = True
  )
  created_at = db.Column(
    db.DateTime,
    index = False,
    unique = False,
    nullable = True,
    default = db.func.current_timestamp()
  )
  deleted_at = db.Column(
    db.DateTime,
    index = False,
    unique = False,
    nullable = True
  )

  def to_json(self):
    res_json = {
      'id' : self.id,
      'sensor_name' : self.sensor_name,
      'mac_address' : self.mac_address,
      'room' : self.room,
      'floor' : self.floor,
      'building' : self.building,
      'location' : self.location,
    }

    return res_json

  def __repr__(self):
    return '<Sensor {}>'.format(self.id)
