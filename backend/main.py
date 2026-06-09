from fastapi import FastAPI, HTTPException
from agents.orchestrator_agent import generate_complete_report

app = FastAPI(
    title="AI Travel Companion API",
    description="Generative AI travel planning API",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "AI Travel Companion API Running"
    }


@app.get("/travel-report")
def travel_report(
    destination: str,
    days: int = 3
):
    try:
        report = generate_complete_report(destination, days)

        return {
            "destination": destination,
            "days": days,
            "report": report
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }