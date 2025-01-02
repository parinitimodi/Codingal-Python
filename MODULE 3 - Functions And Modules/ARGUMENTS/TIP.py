def total_calc(bill_amnt,tip_prc):
    total = bill_amnt*(1 + 0.1 * tip_prc)
    total = round(total,2)
    print(f"Please pay ${total}")

total_calc(10000,20)