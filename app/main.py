from fastapi import FastAPI
from .recommender import Recommender

app = FastAPI()


@app.get("/recommendations/{user_id}")
async def recommend_products(user_id: int):
    recommender = Recommender()
    recommendations = recommender.get_user_recommendations(user_id)
    return {"user_id": user_id, "recommended_products": recommendations}


@app.get("/history_recommendations/{user_id}")
async def recommend_history_products(user_id: int):
    recommender = Recommender(use_history=True)
    recommendations = recommender.get_user_recommendations(user_id)
    return {"user_id": user_id, "recommended_products": recommendations}
