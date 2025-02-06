import pandas as pd
from typing import List
from app.models.payroll_entry import PayrollEntry

def process_csv(file_path: str) -> List[PayrollEntry]:
    df = pd.read_csv(file_path)
    entries = df.to_dict(orient="records")
    return [PayrollEntry(**entry) for entry in entries]
