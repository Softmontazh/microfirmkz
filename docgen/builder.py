# docgen/builder.py

from docxtpl import DocxTemplate
from pathlib import Path


class ContractBuilder:
    def __init__(self, template_path: str):
        self.template_path = Path(template_path)
        self.doc = DocxTemplate(self.template_path)

    def fill_fields(self, context: dict):
        self.doc.render(context)

    def save(self, output_path: str):
        self.doc.save(output_path)
        return f"✅ Договор успешно создан: {output_path}"
