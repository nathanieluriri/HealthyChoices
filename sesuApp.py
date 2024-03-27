import pandas as pd
# import seaborn as sns
import numpy as np
# import matplotlib._pyplot as plt
from scipy.sparse import csr_matrix

import pickle

from sklearn.neighbors import NearestNeighbors


ratings = pd.read_csv("ratings.csv",  names=['User_ID', 'Food_ID', 'Rating'])
food = pd.read_csv("1662574418893344.csv",names=["Food_ID","Name","C_Type","Veg_Non","Describe"])


# print(ratings.head(10))
# print(food.head(10))


ratings['Rating'] = pd.to_numeric(ratings['Rating'], errors='coerce')
ratings['User_ID'] = pd.to_numeric(ratings['User_ID'], errors='coerce')
ratings['Food_ID'] = pd.to_numeric(ratings['Food_ID'], errors='coerce')
food['Food_ID']=pd.to_numeric(food['Food_ID'], errors='coerce')

# print(recommender_pivot.head(10))
recommender_pivot =ratings.pivot_table(columns='User_ID',index='Food_ID',values="Rating")
recommender_pivot.fillna(0, inplace=True)

food_w_rating = ratings.merge(right=food,on='Food_ID')




recommender_sparse=csr_matrix(recommender_pivot)


model = NearestNeighbors(algorithm='brute')

model.fit(recommender_sparse)



#TODO Replace 26 with the value of a food id 
distance ,suggestion =model.kneighbors(recommender_pivot.iloc[26,:].values.reshape(1,-1),n_neighbors=6)

#TODO after getting the suggestion in an array use the index to get the name of the food 

#TODO using the name of the food get directions on how to cook 

#TODO Generate image of food that user wants to eat or cook 

print("distance: ",distance)
print("suggestions:",suggestion)

for i in range(len(suggestion)):
    print(recommender_pivot.index[suggestion[i]])


# pickle.dump(model,open("model.pkl","wb"))
# pickle.dump(food_w_rating,open("food_with_rating.pkl","wb"))
# pickle.dump(recommender_pivot,open("recommender_pivot.pkl","wb"))








books = pd.read_csv("sesu/data.csv",  names=['isbn13', 'isbn10', 'title','subtitle','authors','categories','thumbnail','description','published_year','average_rating','num_pages','ratings_count'])
