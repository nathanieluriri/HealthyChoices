import pickle
import json
import pandas as pd

food_csv = pd.read_csv("1662574418893344.csv",names=["Food_ID","Name","C_Type","Veg_Non","Describe"])
model =pickle.load(open("model.pkl","rb"))
recommender_pivot = pickle.load(open("recommender_pivot.pkl","rb"))
food_with_rating = pickle.load(open("food_with_rating.pkl","rb"))

Ai_response = pickle.load(open("response.pkl","rb"))
Ai_response=Ai_response.replace("'",'"').encode().decode('utf-8')

Ai_response=repr(Ai_response)
Ai_response = Ai_response.strip("'")




try:
    # Attempt to convert the string to a list
    Ai_response_list = json.loads(Ai_response)
    # print(Ai_response_list)
    Food_ID = Ai_response_list[0]
    # print(Food_ID)

    # distance , suggestion =model.kneighbors(recommender_pivot.iloc[Food_ID,:].values.reshape(1,-1),n_neighbors=6)
    # print("distance: ",distance)
    # print("SUggestions",suggestion)
except json.decoder.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")


    
        
def name_of_food():
    Ai_response = pickle.load(open("response.pkl","rb"))
    Ai_response=Ai_response.replace("'",'"').encode().decode('utf-8')

    Ai_response=repr(Ai_response)
    Ai_response = Ai_response.strip("'")
    
    Ai_response_list = json.loads(Ai_response)
   
    Food_name = Ai_response_list[1]
    return Food_name    

def recipe_of_food():
    Ai_response = pickle.load(open("response.pkl","rb"))
    Ai_response=Ai_response.replace("'",'"').encode().decode('utf-8')

    Ai_response=repr(Ai_response)
    Ai_response = Ai_response.strip("'")
    
    Ai_response_list = json.loads(Ai_response)
    print(Ai_response_list)
    Food_recipe = Ai_response_list[2]+Ai_response_list[3]
    return Food_recipe   

def recomend_similar_food():
    Ai_response = pickle.load(open("response.pkl","rb"))
    Ai_response=Ai_response.replace("'",'"').encode().decode('utf-8')

    Ai_response=repr(Ai_response)
    Ai_response = Ai_response.strip("'")
    
    Ai_response_list = json.loads(Ai_response)
    
    FoodID = Ai_response_list[0]
    distance , suggestion =model.kneighbors(recommender_pivot.iloc[FoodID,:].values.reshape(1,-1),n_neighbors=4)
    print(suggestion)
    return [suggestion[0][1],suggestion[0][2],suggestion[0][3]]   






def filter(food_df,food_id):    
    if food_id in food_df["Food_ID"]:
        
        result=food_df[["Name", "C_Type", "Describe"]].iloc[food_id]
        return result.values.tolist()

def recommend_similar_food_func():
    lis=[]
    for foodid in recomend_similar_food():
        lis.append(filter(food_df=food_csv,food_id=foodid))
    return lis
