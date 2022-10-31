from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    product_list = [
        {
            "id": 1,
            "nome_do_produto": "Cafe",
            "nome_da_empresa": "Cafes Nature",
            "data_de_fabricacao": "2020-07-04",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "instrucao",
        }
    ]

    report_color_simple = ColoredReport(SimpleReport)

    report_simple = report_color_simple.generate(product_list)
    assert (
        report_simple
        == "\033[32mData de fabricação mais antiga:\033[0m "
        + "\033[36m2020-07-04\033[0m"
        + "\n\033[32mData de validade mais próxima:\033[0m "
        + "\033[36m2023-02-09\033[0m"
        + "\n\033[32mEmpresa com mais produtos:\033[0m "
        + "\033[31mCafes Nature\033[0m"
    )
