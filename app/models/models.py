"""
Author: Harold
Date: 19-12-18
---------------------

"""
from datetime import date
import json

class User:
    def __init__(self,id,**kwargs):
        self.id=id
        self.firstname = kwargs['firstname']
        self.lastname = kwargs['lastname']
        self.othernames = kwargs['othernames']
        self.email = kwargs['email']
        self.phoneNumber = kwargs['phoneNumber']
        self.username = kwargs['username']
        self.registered=date.today()
        self.isAdmin = kwargs['isAdmin']


    def convert_to_dictionary(self):
        return {'id': self.id, 'name': self.firstname,'name': self.lastname,
                'othernames': self.othernames,'email':self.email, 
                'phoneNumber':self.phoneNumber, 'username':self.username,
                'registered':self.registered,'isAdmin':self.isAdmin}


class Incident:
    def __init__(self,id,createdBy,types,**kwargs):

        # created default for the instance varaibles
        self.id = id
        self.createdOn = date.today()
        self.createdBy = createdBy
        self.types = types
        self.location = kwargs['location']
        self.status ='draft'
        self.Images = kwargs['Images']
        self.Videos = kwargs['Videos']
        self.comment = kwargs['comment']


    def validate_data(createdBy):
        if not isinstance(createdBy, str):
            return False

        return True

    def convert_to_dictionary(self):
        return {'id': self.id, 'createdOn':self.createdOn,'createdBy':self.createdBy,
                'types':self.types,'location':self.location,'status':self.status,'Images':self.Images,
                'Videos':self.Videos,'comment':self.comment}

    


