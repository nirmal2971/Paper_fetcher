import pandas as pd
from typing import List, Dict

def is_non_academic_author(affiliation: str) -> bool:
    if not affiliation:
        return False
    academic_keywords = ["university", "college", "institute", "hospital", "school"]
    return not any(word in affiliation.lower() for word in academic_keywords)

def save_to_csv(data: List[Dict], filename: str):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
