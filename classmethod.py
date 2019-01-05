# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Data_test(object):
    day = 0
    month = 0
    year = 0
    def __init__(self,year=0,month=0,day=0):
        self.day = day
        self.month = month
        self.year = year
    @classmethod
    def get_date(cls,data_as_string):
        year,month,day = map(int,data_as_string.split('-'))
        date1 = cls(year,month,day)
        return date1
    def out_date(self):
        print("year:")
        print(self.year)
        print("month")
        print(self.month)
        print("day")
        print(self.day)
        
#t = Data_test(2016,8,1)
#t.out_date()
r = Data_test().get_date('2016-8-6')
r.out_date()