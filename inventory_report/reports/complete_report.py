from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def store_products_by_entreprise(cls, list):
        result = ""
        products_by_entreprise = Counter(
            [item["nome_da_empresa"] for item in list]
        )

        for entreprise, qty in products_by_entreprise.items():
            result += f"- {entreprise}: {qty}\n"

        return result

    @classmethod
    def generate(cls, list):
        products_by_entreprise = CompleteReport.store_products_by_entreprise(
            list
        )

        return (
            super().generate(list)
            + "\nProdutos estocados por empresa:\n"
            + products_by_entreprise
        )
