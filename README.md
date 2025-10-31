# taxcalculator
TaxCalculator - a kata for a Clean Code exercise
Structure of my solution:
- File with the constants, such as tax rates.
- Test_TaxCalculator: for two different inputs, print the original output and the output of my solution.
- TaxSimulator: gather and verify user inputs, call a TaxCalculator to calculate taxes, and then a taxPrinter to print those.
- TaxCalculator: Civil and Employee contracts can be treated the same way, therefore, I created a super class. The only tax that depends on
the type of contract is handled by an abstract method, which is implemented into two different child classes. The result is stored in dictionnary.
- TaxPrinter: Use the dictionnary made by taxCalculator t print taxes to user.

Additional remarks:
The different taxes names aren't revelant to me, I tried to make those fit with the string message corresponding, even if it's not always meaningful.
I kept a few prints in TaxSimulator.main() to avoid pounderousness in TaxPrinter.
I tried to leave from main as soon as possible.


