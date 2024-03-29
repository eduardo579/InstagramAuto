import json
from datetime import datetime

class Post:
    def __init__(self, description, image, post_date, has_been_posted):
        self.image = image
        self.description = description
        self.post_date = post_date
        self.has_been_posted = has_been_posted
    
    def serialize(self):
        date = self.post_date.strftime("2019-12-17 11:55:00")
        return {
            'image' : self.image,
            'description' : self.description,
            'post_date' : date,
            'has_been_posted' : self.has_been_posted
        }