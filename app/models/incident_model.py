"""
Author: Harold
Date: 19-12-18
---------------------

"""
from datetime import date
import json

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

    


