from unittest import TestCase

from TaxSimulator import TaxSimulator


class TestTaxCalculator(TestCase):
    def test_main(self):
        TaxSimulator(3000.0, "E").main()
        print("""EMPLOYMENT
                    Income  3000.0
                    Social security tax: 292.80
                    Health social security tax: 45.00
                    Sickness social security tax: 73.50
                    Income for calculating health security tax:  2588.7
                    Healt social security tax: 9% = 232.98 7,75% = 200.62
                    Tax deductible expenses:  111.25
                    Income to be taxed:  2477.45  rounded: 2477
                    Advance tax 18% =  445.85999999999996
                    Tax free income = 46.33
                    AlreadyPaid= 399.53
                    Paid advance tax = 198.91 rounded 199
                    Net income = 2156.72""")
        TaxSimulator(2500.0, "C").main()
        print(f"""CIVIL
                Income 2500.0
                Social security tax: 244.0
                Health social security tax: 37.5
                Sickness social security tax: 61.25
                Income for calculating health security tax: 2157.25
                Health security tax: 9%: 194.15
                Health security tax: 7.75%: 167.19
                Tax deductible expenses: 431.45
                Income to be taxed: 1725.8
                Rounded Income to be taxed: 1726
                Advance tax: 18%: 310.68
                Already paid tax: 310.68
                Advance tax: 143.49
                Rounded advance tax: 143
                Net income: 1820.1""")
        TaxSimulator(187.0, "invalide").main()

