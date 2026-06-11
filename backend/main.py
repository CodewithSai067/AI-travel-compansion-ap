from fastapi import FastAPI
from agents.orchestrator_agent import generate_complete_report
import anyio

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Travel Companion API Running"}

@app.get("/travel-report")
async def travel_report(destination: str, days: int, budget: int):
    # This securely offloads your AI multi-agent processing to a separate thread
    report = await anyio.to_thread.run_sync(
        generate_complete_report, 
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