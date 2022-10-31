import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) != 3:
        return sys.stderr.write("Verifique os argumentos\n")

    _, path, report_type = sys.argv

    report = None

    if path.endswith(".csv"):
        report = InventoryRefactor(CsvImporter)

    if path.endswith(".json"):
        report = InventoryRefactor(JsonImporter)

    if path.endswith(".xml"):
        report = InventoryRefactor(XmlImporter)

    print(report.import_data(path, report_type), end="")
