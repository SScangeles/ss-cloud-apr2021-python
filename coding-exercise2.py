
## 1) Numbers

num_ex1 = 10 + 10
num_ex2 = 5 - 1

print(num_ex1, num_ex2, num_ex1 + num_ex2)

## 2) Output for: 30+*6, 6^6, 6**6, 6+6+6+6+6+6

# out_ex1 = 30+*6
out_ex2 = 6^6
out_ex3 = 6**6
out_ex4 = 6+6+6+6+6+6

print(out_ex2, out_ex3, out_ex4)

## 3) "Hello World"

print("Hello World", "\nHello World :", 10)

## 4) Mortgage Calc

orginal_principle = 800000
new_principle = orginal_principle
rate = 0.06
monthly_payments = 10000
months = 103

for x in range(months-1):
    new_principle += (new_principle * (rate/12)) - monthly_payments
    round(new_principle)

last_payment = round(new_principle + (new_principle * (rate/12)))

payout = (months-1) * monthly_payments + last_payment

percentage = (payout - orginal_principle) / orginal_principle