from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def get_date_most_old(cls, list):

        return min(
            datetime.fromisoformat(item["data_de_fabricacao"]).date()
            for item in list
        )

    @classmethod
    def get_date_most_close(cls, list):
        return min(
            datetime.fromisoformat(item["data_de_validade"]).date()
            for item in list
            if datetime.fromisoformat(item["data_de_validade"])
            > datetime.now()
        )

    @classmethod
    def get_enterprise_most_products(cls, list):
        return Counter(
            [item["nome_da_empresa"] for item in list]
        ).most_common()[0][0]

    @classmethod
    def generate(cls, list):

        most_old = SimpleReport.get_date_most_old(list)

        most_close = SimpleReport.get_date_most_close(list)

        most_products = SimpleReport.get_enterprise_most_products(list)

        return (
            f"Data de fabricação mais antiga: {most_old}\n"
            f"Data de validade mais próxima: {most_close}\n"
            f"Empresa com mais produtos: {most_products}"
        )
