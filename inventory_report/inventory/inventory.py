import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def open_file(cls, path):
        if path.endswith(".csv"):
            with open(path) as file:
                return list(csv.DictReader(file))

        if path.endswith(".json"):
            with open(path) as file:
                return list(json.load(file))

        if path.endswith(".xml"):
            with open(path) as file:
                return xmltodict.parse(file.read())["dataset"]["record"]

    @classmethod
    def import_data(cls, path, type):

        data = Inventory.open_file(path)
        print(data)
        if type == "simples":
            return SimpleReport.generate(data)

        if type == "completo":
            return CompleteReport.generate(data)
