import google.generativeai as genai

genai.configure(api_key="AIzaSyBBTsAplxkTkHYofKyTp_1qfqOw55hoK9I")

model = genai.get_model('models/embedding-gecko-001')
embeddings=genai.generate_embeddings(model=model,text="I want to embed")
print(embeddings)