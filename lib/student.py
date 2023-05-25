#!/usr/bin/env python

from user import User

#  The Student class inherits from the User class and has an empty 'knowledge' list.
#     The 'learn' method appends information to the 'knowledge' list.

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    
    def learn(self, information):
        self.knowledge.append(information)