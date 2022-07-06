deposit_sum = float (input())
month_period_deposit = int (input())
annual_interest = float (input())

final_sum = deposit_sum + month_period_deposit * ((deposit_sum * annual_interest / 100)/12)
print(final_sum)



#сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
