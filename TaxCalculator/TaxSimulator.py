from Constants import TAXATION_RATE_SOCIAL_SECURITY_SICKNESS, TAXATION_RATE_SOCIAL_SECURITY_HEALTH, \
    TAXATION_RATE_SOCIAL_SECURITY, TAXATION_RATE_ADVANCE_18, TAXATION_RATE_HEALTH_2, TAXATION_RATE_HEALTH_1, \
    DEDUCTIBLE_EXPANSES_RATE
from TaxCalculator import TaxCalculator
from TaxCalculator import TaxCalculatorEmployeeContract, TaxCalculatorCivilContract
from TaxPrinter import TaxPrinter


class TaxSimulator():
    taxCalculator: TaxCalculator

    def __init__(self, income: float = None, contractType: str = None):
        self.income = income
        self.contractType = contractType

    def main(self):
        if (self.income is None) or (self.contractType is None):
            self.tryGetUserInputs()
        if (self.income is None) or (self.contractType is None):
            return
        taxCalculator = self.chooseCalculator()
        if taxCalculator is None:
            return
        taxCalculator.calculateTaxes()
        taxesDictionnary = taxCalculator.getTaxesDictionnary()
        taxPrinter = TaxPrinter(taxesDictionnary)
        taxPrinter.printTaxCalculus()
        return

    def tryGetUserInputs(self):
        try:
            self.income = float(input("Enter income: "))
            self.contractType = input("Contract Type: (E)mployment, (C)ivil")[0]
        except ValueError:
            print("Incorrect")

    def chooseCalculator(self):
        if self.contractType == "E":
            print("EMPLOYMENT")
            print("Income ", self.income)
            return TaxCalculatorEmployeeContract(self.income)

        elif self.contractType == "C":
            print("CIVIL")
            print("Income", self.income)
            return  TaxCalculatorCivilContract(self.income)

        else:
            print("Unknowne type of contract!")
            return None



if __name__ == '__main__':
    TaxSimulator().tryGetUserInputs()

