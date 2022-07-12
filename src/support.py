import pandas as pd

class Cleaning():
    def __init__(self, df):
        self.df = df
    
    def get_month(self, column_name):

        self.column_name = column_name


        if type(column_name) == str:
            return column_name.split()[0] 
        else: 
            return column_name
    
    
    def get_year(self, column_name):

        self.column_name = column_name

        if type(column_name) == str:
            try: 
                return column_name.split(",")[1]
            except: 
                return column_name.split(".")[1]
        else: 
            pass

    
    def split_column(self, column_name):

        self.column_name = column_name

        if type(column_name) == str:
            return column_name.split(',')
        
        else: 
            return column_name







