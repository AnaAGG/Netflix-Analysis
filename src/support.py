import pandas as pd

class Cleaning():
    def __init__(self, df, premiere_column, cast_director_column):
        self.df = df
        self.premiere_column = premiere_column
        self.cast_director_column = cast_director_column


    def get_month(self):

        if type(self.premiere_column) == str:
            return self.premiere_column.split()[0] 
        else: 
            return self.premiere_column
        
        
    
    def get_year(self):

        if self.df[self.premiere_column].dtypes== "O":
            try: 
                
                return self.df[self.premiere_column].str.split(",", n = 1).str.get(1)
            except: 
                return self.df[self.premiere_column].str.split(".", n = 1).str.get(1)
        else: 
            pass

    
    def split_column(self):

        if type(self.cast_director_column ) == str:
            return self.cast_director_column .split(',')
        
        else: 
            return self.cast_director_column 


    def clean(self): 

        self.df["month"] = self.df.apply(lambda x: self.get_month(), axis = 1)
        results = self.df.apply(lambda x: self.get_year(), axis=1)
        self.df[self.cast_director_column] = self.df.apply(lambda x:self.split_column(), axis=1)

        print(results)
        self.df.to_csv("prbamdo_clase.csv")

        return self.df







