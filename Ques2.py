print("Welcome!")
print("\nTAX Calculator")
def tax(gi=None, nd=None, t=None, ti=None):
    ti = gi - 10000 - (3000 * nd)
    t = ti * (0.2)
    if t > 0:
        return t

gi = float(input("\nEnter the Gross Income(in $) : "))
nd = int(input("Enter the number of dependents : "))
print("\nThe TAX to be paid by you in $ is : ", tax(gi, nd))