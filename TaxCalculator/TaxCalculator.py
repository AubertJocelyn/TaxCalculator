from abc import ABC, abstractmethod

from Constants import DEDUCTIBLE_EXPANSES_RATE, TAXATION_RATE_ADVANCE_18, \
    TAXATION_RATE_SOCIAL_SECURITY, TAXATION_RATE_SOCIAL_SECURITY_HEALTH, TAXATION_RATE_SOCIAL_SECURITY_SICKNESS, \
    TAXATION_RATE_HEALTH_1, TAXATION_RATE_HEALTH_2


class TaxCalculator(ABC):
    reduceTax: float
    t_socialSecurity = 0
    t_socialSecurityHealth = 0
    t_socialSecuritySickness = 0
    expensesDeductibleFromTaxes: float
    t_health1 = 0
    t_health2 = 0
    t_advance_18 = 0
    reducedTax = 46.33
    advanceTax = 0
    advanceTaxRounded = 0

    def __init__(self, income):
        self.income = income

    def getTaxesDictionnary(self):
        return {
            "Social security tax": round(self.t_socialSecurity, 2),
            "Health social security tax": round(self.t_socialSecurityHealth, 2),
            "Sickness social security tax": round(self.t_socialSecuritySickness, 2),
            "Income for calculating health security tax": self.incomeAfterSocialSecurityTaxes,
            "Health security tax: 9%": round(self.t_health1, 2),
            "Health security tax: 7.75%": round(self.t_health2, 2),
            "Tax deductible expenses": self.expensesDeductibleFromTaxes,
            "Income to be taxed": self.taxableIncomeAfterDeductions,
            "Rounded Income to be taxed": round(self.taxableIncomeAfterDeductions),
            "Advance tax: 18%": self.t_advance_18,
            "Already paid tax": round(self.taxPaid, 2),
            "Advance tax": round(self.advanceTax, 2),
            "Rounded advance tax": round(self.advanceTax),
            "Net income": round(self.netIncome, 2)
            }
    
    def setAdvancedTax(self):
        self.advanceTax = self.t_advance_18 - self.t_health2 - self.reducedTax

    def setAdvanceTax18(self):
        self.t_advance_18 = self.roundedTaxableIncomeAfterDeductions * TAXATION_RATE_ADVANCE_18

    def setIncomeAfterSocialSecurityTaxes(self):
        self.incomeAfterSocialSecurityTaxes = (self.income - self.t_socialSecurity - self.t_socialSecurityHealth - self.t_socialSecuritySickness)

    def setSocialSecurityTaxes(self):
        self.t_socialSecurity = self.income * TAXATION_RATE_SOCIAL_SECURITY
        self.t_socialSecurityHealth = self.income * TAXATION_RATE_SOCIAL_SECURITY_HEALTH
        self.t_socialSecuritySickness = self.income * TAXATION_RATE_SOCIAL_SECURITY_SICKNESS

    def setHealthTaxesOneAndTwo(self):
        self.t_health1 = self.incomeAfterSocialSecurityTaxes * TAXATION_RATE_HEALTH_1
        self.t_health2 = self.incomeAfterSocialSecurityTaxes * TAXATION_RATE_HEALTH_2

    def setTaxableIncomeAfterDeductions(self):
        self.taxableIncomeAfterDeductions = self.incomeAfterSocialSecurityTaxes - self.expensesDeductibleFromTaxes

    def setNetIncome(self):
        self.netIncome = self.income - ((self.t_socialSecurity + self.t_socialSecurityHealth
                                         + self.t_socialSecuritySickness) + self.t_health1 + self.advanceTaxRounded)

    def setTDeductibleExpanses(self):
        self.expensesDeductibleFromTaxes = round(self.incomeAfterSocialSecurityTaxes * DEDUCTIBLE_EXPANSES_RATE, )

    def setRoundedTaxableIncomeAfterDeductions(self):
        self.roundedTaxableIncomeAfterDeductions = round(self.taxableIncomeAfterDeductions)

    def setTaxPaid(self):
        self.taxPaid = self.t_advance_18 - self.reducedTax


    def calculateTaxes(self):
        self.setSocialSecurityTaxes()
        self.setIncomeAfterSocialSecurityTaxes()
        self.setHealthTaxesOneAndTwo()
        self.setTDeductibleExpanses()
        self.setTaxableIncomeAfterDeductions()
        self.setRoundedTaxableIncomeAfterDeductions()
        self.setAdvanceTax18()
        self.setTaxPaid()
        self.setAdvancedTax()
        self.advanceTaxRounded = round(self.advanceTax)
        self.setNetIncome()

    @abstractmethod
    def setTaxableIncomeAfterDeductions_(self):
        pass

class TaxCalculatorCivilContract(TaxCalculator):
    def __init__(self, income):
        super().__init__(income)
        self.reducedTax = 0
        
    def setTaxableIncomeAfterDeductions_(self):
        self.expensesDeductibleFromTaxes = self.incomeAfterSocialSecurityTaxes * DEDUCTIBLE_EXPANSES_RATE

class TaxCalculatorEmployeeContract(TaxCalculator):
    def __init__(self, income):
        super().__init__(income)
        self.reducedTax = 46.33
       
    def setTaxableIncomeAfterDeductions_(self):
        self.expensesDeductibleFromTaxes = 111.25



