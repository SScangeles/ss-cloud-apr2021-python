
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

principle = 800000
rate = 0.06
monthly_payments = 10000
months = 103

for x in range(months-1):
    principle += (principle * (rate/12)) - monthly_payments

last_payment = principle + (principle * (rate/12))

payout = (months - 1) * monthly_payments + last_payment

print("Mortgage payout: ", payout)