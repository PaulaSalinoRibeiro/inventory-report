from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, importer: Importer):
        self.importer = importer
        self.data = []

    def open_file(self, path):
        data_list = self.importer.import_data(path)
        self.data.extend(data_list)

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, type):

        self.open_file(path)

        if type == "simples":
            return SimpleReport.generate(self.data)

        if type == "completo":
            return CompleteReport.generate(self.data)
