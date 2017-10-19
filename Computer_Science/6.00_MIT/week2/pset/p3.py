"""
    This module is a p2.py in steroids. It returns the minimum
    monthly payment without it needing to be a multiple of 10.
"""


def balance_next_month(balance, annual_interest_rate, monthly_payment):
    """
        balance: int or float
        interest_rate: float between 0 and 1
        payment_rate: float between 0 and 1

        returns: card balance after one month if you pay only the minimum payment
    """
    unpaid_balance = balance - monthly_payment
    return unpaid_balance * (1 + annual_interest_rate / 12)


def balance_next_year(balance, annual_interest_rate, monthly_payment):
    """
        balance: int or float
        interest_rate: float between 0 and 1
        payment_rate: float between 0 and 1

        returns: card balance after one year if you pay only the minimum payment
    """
    for _ in range(12):
        balance = balance_next_month(
            balance, annual_interest_rate, monthly_payment)
    return round(balance, 2)


def get_minimum_payment(balance, annual_interest_rate):
    """
        balance: int or float
        interest_rate: float between 0 and 1
        payment_rate: float between 0 and 1

        returns: minimum monthly payment to pay balance in 12 months
    """
    lower_bound = balance / 12
    upper_bound = (balance * (1 + annual_interest_rate / 12) ** 12) / 12
    payment = (lower_bound + upper_bound) / 2
    error = balance_next_year(balance, annual_interest_rate, payment)
    while error != 0:
        if error > 0:
            lower_bound = payment
            payment = (payment + upper_bound) / 2
        else:
            upper_bound = payment
            payment = (lower_bound + payment) / 2
        error = balance_next_year(balance, annual_interest_rate, payment)
    return round(payment, 2)


print(get_minimum_payment(320000, 0.2))
