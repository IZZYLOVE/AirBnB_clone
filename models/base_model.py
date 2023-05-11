#!/usr/bin/python3

"""This is the base model of all objects in the Airbnb web project.


   Description: The base_model of the Hbnb project, "a clone of the
   Airbnb website" is a file that contains the programming
   construct to create a class that in turn create objects that will
   be used to create and control the workings of the hbnb website.
"""

import datetime
import uuid
import re


class BaseModel:

    """Base class of the of the hbnb project.


       Description: This is the base class of the hbnb project it is the
       base factory of all objects for the hbnb project.

       @id: unique 128 bit id that is randomly generated and assign to every
       newly created object.
       @created_at: Holds the date and time an object was created.
       @updated_at: Holds the date and time of a newly updated instance object.
    """

    def __init__(self, *args, **kwargs):

        """Initializes the instances objects of the base class."""

        if kwargs is None:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
        else:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                if k == "created_at":
                    delimeters = r"[-.:T]"
                    d = re.split(delimeters, v)
                    self.k = datetime.datetime(int(d[0]), int(d[1]), int(d[2]),
                                               hour=int(d[3]),
                                               minute=int(d[4]),
                                               seconds=int(d[5]),
                                               microsecond=int(d[6]))
                if k == "updated_at":
                    delimeters = r"[-.:T]"
                    d = re.split(delimeters, v)
                    self.k = datetime.datetime(int(d[0]), int(d[1]), int(d[2]),
                                               hour=int(d[3]),
                                               minute=int(d[4]),
                                               seconds=int(d[5]),
                                               microsecond=int(d[6]))
                self.k = v

    def __str__(self):

        """Returns the string representation of the object."""

        hbnb_Bobj_str = "[{}] ({}) {}".format("BaseModel",
                                              self.id, self.__dict__)
        return hbnb_Bobj_str

    def save(self):

        """Updates the public instance variable updated_at to the current date
           time object.
        """

        self.updated_at = datetime.datetime.now()

    def to_dict(self):

        """Returns the dictionary representation of the object."""

        hbnb_obj_dict = self.__dict__
        hbnb_obj_dict["__class__"] = "BaseModel"
        hbnb_obj_dict["created_at"] = self.created_at.isoformat()
        hbnb_obj_dict["updated_at"] = self.updated_at.isoformat()
        return hbnb_obj_dict
