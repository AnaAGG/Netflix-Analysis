# Adding the parent directory to the path.
import sys
sys.path.append('../')


# Importing the pandas library and renaming it to pd.
import pandas as pd

# Importing the support module from the src directory.
import src.support as sp


# Reading the csv file and assigning it to the variable `originals`, that contains the Netflix original titles
originals = pd.read_csv("../data/netflix_originals.csv", index_col = 0)

# Reading the csv file and assigning it to the variable `df`, which contains all the TV Shows and Movies that we can see in Netflix
df= pd.read_csv("../data/netflix_titles.csv")


# Merging the two dataframes `df` and `originals` on the column `title` and `Title` respectively, to get only the original Netflix movies based on the movies that we have in the df datafram
originals_df = df.merge(originals, left_on= "title", right_on="Title", how="inner")

c = sp.Cleaning(originals_df, "Premiere", "cast")

df = c.clean()