from pydantic import BaseModel, EmailStr

class PayrollEntry(BaseModel):
    full_name: str
    email: EmailStr
    position: str
    health_discount_amount: float
    social_discount_amount: float
    taxes_discount_amount: float
    other_discount_amount: float
    gross_salary: float
    gross_payment: float
    net_payment: float
    period: str
