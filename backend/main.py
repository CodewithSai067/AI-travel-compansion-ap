from fastapi import FastAPI
from agents.orchestrator_agent import generate_complete_report

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Travel Companion API Running"}

@app.get("/travel-report")
def travel_report(
    destination: str,
    days: int,
    budget: int
):
    report = generate_complete_report(
        destination,
        days,
        budget
    )

    return {
        "destination": destination,
        "days": days,
        "budget": budget,
        "report": report
    }