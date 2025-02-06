from fastapi import FastAPI
from app.routes import payroll

app = FastAPI(
    title="Paystub Notifier API",
    description="API para procesar planillas, generar recibos de pago y enviarlos por correo electrónico.",
    version="1.0.0"
)

app.include_router(payroll.router, prefix="/api", tags=["Payroll"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=3000, reload=True)
