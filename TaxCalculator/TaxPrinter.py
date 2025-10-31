class TaxPrinter():
    def __init__(self, taxesDictionnary: dict):
        self.taxesDictionnary = taxesDictionnary
    def printTaxCalculus(self):
        for taxeName in self.taxesDictionnary.keys():
            taxeValue: float = self.taxesDictionnary[taxeName]
            print(f"{taxeName}: {taxeValue}")
