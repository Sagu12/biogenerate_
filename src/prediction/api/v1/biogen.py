from fastapi import APIRouter
from src.prediction.services.v1.biogenv2 import BioGen
from fastapi import FastAPI, Form


BioGeneration= BioGen()
predict= APIRouter()

keywords = ['Adventurous',
 'Ambitious',
 'Ambivert',
 'Artist',
 'BikeLover',
 'Calm',
 'CarLover',
 'Caring',
 'ChaiLover',
 'Charming',
 'Cheerful',
 'Chocaholic',
 'CoffeeLover',
 'Creative',
 'Curious',
 'Danceaholic',
 'DogLover',
 'Dreamer',
 'Emotional',
 'Energetic',
 'Entertainer',
 'Entrepreneur',
 'Extrovert',
 'Faithful',
 'Feminist',
 'FitnessFreak',
 'Foodie',
 'Friendly',
 'Funny',
 'GadgetLover',
 'GameAddict',
 'Geek',
 'Independent',
 'Intellectual',
 'Introvert',
 'Kind',
 'Loyal',
 'Moody',
 'Motivated',
 'MovieManiac',
 'MusicLover',
 'Mysterious',
 'NatureLover',
 'Nightowl',
 'OpenMinded',
 'Optimistic',
 'PartyHopper',
 'Reader',
 'Romantic',
 'Sapiosexual',
 'Sarcastic',
 'Sexy',
 'Shopaholic',
 'Shy',
 'Simple',
 'Spiritual',
 'SportsFanatic',
 'Stylish',
 'Talkative',
 'Techie',
 'Traveller',
 'Workaholic',
 'Writer']

@predict.post("/keywords")
async def get_keywords():
    return {"keywords": keywords}

@predict.post('/text_detect')
async def api_predict(keywords: str) -> None:
    return await BioGeneration.main(keywords)