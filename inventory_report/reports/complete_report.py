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
        most_old = super().get_date_most_old(list)

        most_close = super().get_date_most_close(list)

        most_products = super().get_enterprise_most_products(list)

        products_by_entreprise = CompleteReport.store_products_by_entreprise(
            list
        )

        return (
            f"Data de fabricação mais antiga: {most_old}\n"
            f"Data de validade mais próxima: {most_close}\n"
            f"Empresa com mais produtos: {most_products}"
            + "\nProdutos estocados por empresa:\n"
            + products_by_entreprise
        )
