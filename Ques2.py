print("Welcome!")
print("\nTAX Calculator")
def tax(gi, nd, t=None, ti=None):
    ti = gi - 10000 - (3000 * nd)
    t = ti * (0.2)
    return t

gi = float(input("\nEnter the Gross Income(in $) : "))
nd = int(input("Enter the number of dependents : "))
print("\nThe TAX to be paid by you in $ is : ", tax(gi, nd))