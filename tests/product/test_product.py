from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Produto",
        "Empresa",
        "28-10-2022",
        "28-10-2023",
        "xml123",
        "Armazenamento",
    )
    assert type(product.id) == int
    assert product.id == 1
    assert type(product.nome_da_empresa) == str
    assert product.nome_da_empresa == "Empresa"
    assert type(product.nome_do_produto) == str
    assert product.nome_do_produto == "Produto"
    assert type(product.data_de_fabricacao) == str
    assert product.data_de_fabricacao == "28-10-2022"
    assert type(product.data_de_validade) == str
    assert product.data_de_validade == "28-10-2023"
    assert type(product.numero_de_serie) == str
    assert product.numero_de_serie == "xml123"
    assert type(product.instrucoes_de_armazenamento) == str
    assert product.instrucoes_de_armazenamento == "Armazenamento"
