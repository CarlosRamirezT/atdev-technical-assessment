from fastapi import FastAPI
from app.routes import payroll

app = FastAPI(
    title="Paystub Notifier API",
    description="API for processing payroll CSV files and sending paystub PDFs via email.",
    version="1.0.0"
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Paystub Notifier API"}

app.include_router(payroll.router, prefix="/api", tags=["Payroll"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=3000, reload=True)
