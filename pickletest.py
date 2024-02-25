import pickle

model =pickle.load(open("model.pkl","rb"))
recommender_pivot = pickle.load(open("recommender_pivot.pkl","rb"))


# model.kneighbors(recommender_pivot.iloc[26,:].values.reshape(1,-1),n_neighbors=6)

print(recommender_pivot.head(26))

print(recommender_pivot.iloc[23,0:3].values)


