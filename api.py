from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
from google.genai import types

app: FastAPI = FastAPI()

load_dotenv()
client: genai.Client = genai.Client()

# Define a Pydantic model for the request body
class Review(BaseModel):
    content: str

class ReviewFeedback(BaseModel):
    prompt: str
    model: str = "models/text-bison-001"
    temperature: float = 0.7
    max_output_tokens: int = 256
    review_prompt: str = "Please provide a review of the following text."

# What Gemini model must give back, what we SEND to the user (the response)
# We keep it small on purpose -> fewer tokens, less cost, faster response time

class Analyze(BaseModel):
    label: str #"positive", "negative" or "neutral"
    score: float  # 1 (very bad) to 5 (very good)
    theme: str # one word: what the review is about, e.g. "food", "service", "ambience", etc.


@app.post("/analyze_feedback")
async def analyze_feedback(review: Review) -> Analyze:
    
    interaction = client.interactions.create(
        model="gemini-3.5-flash",

        # Construct the prompt for the model
        input=(
            "Analyze this customer review."
            "label must be one of these: positive, negative or neutral. "
            "score must be a float between 1 (very bad) to 5 (very good)."
            "theme must be ONE lowercase word: what the review is about, e.g. 'food', 'service', 'ambience', etc."
            f"Review: {review.content}"
        ),
        response_format={
                "type": "text",
                "mime_type": "application/json",
                "schema": Analyze.model_json_schema()
        },
        generation_config={
            "temperature": 0.7
        },
    )

    response = Analyze.model_validate_json(interaction.output_text)
    return response