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

