"""
Author: Harold
Date: 19-12-18
---------------------

"""
from random import randint
from datetime import date

class User:
    def __init__(self,firstname,lastname,othernames,
                email,phoneNumber,username,isAdmin):
        self.id=randint(10000,99999)
        self.firstname=firstname
        self.lastname=lastname
        self.othernames=othernames
        self.email=email
        self.phoneNumber=phoneNumber
        self.username=username
        self.registered=date.today()
        self.isAdmin=isAdmin

    def convert_to_dictionary(self):
        return {'id': self.id, 'name': self.firstname,'name': self.lastname,
                'othernames': self.othernames,'email':self.email, 
                'phoneNumber':self.phoneNumber, 'username':self.username,
                'registered':self.registered,'isAdmin':self.isAdmin}


class Incident:
    def __init__(self,createdBy,types,location,status,
                Images,Videos,comment):

        self.id=randint(1,99)
        self.createdOn=date.today()
        self.createdBy=createdBy
        self.types=types
        self.location=location
        self.status=status
        self.Images=Images
        self.Videos=Videos
        self.comment=comment

    def convert_to_dictionary(self):
        return {'id': self.id, 'createdOn':self.createdOn,'createdBy':self.createdBy,
                'types':self.types,'location':self.location,'status':self.status,'Images':self.Images,
                'Videos':self.Videos,'comment':self.comment}