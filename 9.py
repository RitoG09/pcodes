import wikipedia, json, re
from pydantic import BaseModel
from typing import Optional

class InstituteDetails(BaseModel):
    name: str
    founded_year: Optional[str] = None
    summary: str

def extract_details(name):
    try:
        page = wikipedia.page(name)
        year = re.search(r"\b(18|19|20)\d{2}\b", page.content)

        return InstituteDetails(
            name=page.title,
            founded_year=year.group() if year else None,
            summary=wikipedia.summary(name, sentences=6)
        )

    except Exception as e:
        return InstituteDetails(
            name=name,
            summary=f"Error: {e}"
        )

name = input("Enter Institute Name: ")
print(json.dumps(extract_details(name).model_dump(), indent=4))