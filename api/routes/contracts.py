# api/routes/contracts.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from docgen.builder import ContractBuilder
from pathlib import Path
import uuid

router = APIRouter()

TEMPLATES_DIR = Path("templates/contracts")
GENERATED_DIR = Path("generated")
GENERATED_DIR.mkdir(parents=True, exist_ok=True)


class ContractRequest(BaseModel):
    template_name: str
    context: dict


@router.post("/generate")
def generate_contract(data: ContractRequest):
    template_path = TEMPLATES_DIR / data.template_name
    if not template_path.exists():
        raise HTTPException(status_code=404, detail="Template not found")

    file_id = uuid.uuid4().hex
    output_file = GENERATED_DIR / f"contract_{file_id}.docx"

    builder = ContractBuilder(str(template_path))
    builder.fill_fields(data.context)
    builder.save(str(output_file))

    return {"message": "Contract generated", "file": str(output_file)}
