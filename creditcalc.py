import argparse
from math import ceil, floor, log

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=int)
args = parser.parse_args()

if args.type == "diff":
    if args.principal and args.periods and args.interest:
        principal, n, i = args.principal, args.periods, (args.interest / 100) / 12
        m = 0
        over = 0
        for _ in range(n):
            m += 1
            dm = (principal / n) + i * (principal - ((principal * (m - 1)) / n))
            print(f"Month {m}: payment is {ceil(dm)}")
            over += ceil(dm)
        print(f"\nOverpayment = {round(over - principal)}")
    else:
        print("Incorrect parameters.")

elif args.type == "annuity":
    if args.principal and args.payment and args.interest:
        principal, monthly, nominal = args.principal, args.payment, (args.interest / 100) / 12
        year = 0
        total_months = (ceil(log(monthly / (monthly - nominal * principal), 1 + nominal)))
        month_count = total_months % 12
        for x in range(1, total_months + 1):
            if x % 12 == 0:
                year += 1
        overpayment = ceil((monthly * total_months) - principal)
        if month_count == 1:
            print("It will take 1 month to repay this loan!")
        elif month_count > 1 and year == 0:
            print(f"It will take {month_count} months to repay this loan!")
        elif year == 1 and month_count == 0:
            print("It will take 1 year to repay this loan!")
        elif year > 1 and month_count == 0:
            print(f"It will take {year} years to repay this loan!")
        elif year > 1 and month_count == 1:
            print(f"It will take {year} years and 1 month to repay this loan!")
        elif year > 1 and month_count > 1:
            print(f"It will take {year} years and {month_count} months to repay this loan!")
        print(f"Overpayment = {overpayment}")

    elif args.principal and args.periods and args.interest:
        principal, total_months, interest = args.principal, args.periods, (args.interest / 100) / 12
        result = ceil(principal * ((interest * ((1 + interest) ** total_months))
                                   / (((1 + interest) ** total_months) - 1)))
        print(f"Your monthly payment == {result}!")
        print(f"Overpayment = {round((result * total_months) - principal)}")

    elif args.payment and args.periods and args.interest:
        annuity, total_months, interest = args.payment, args.periods, (args.interest / 100) / 12
        result = annuity / ((interest * ((1 + interest) ** total_months)) / (((1 + interest) ** total_months) - 1))
        print(f"Your loan principal = {floor(result)}!")
        print(f"Overpayment = {ceil((annuity * total_months) - result)}")

    else:
        print("Incorrect parameters.")
else:
    print("Incorrect parameters.")
