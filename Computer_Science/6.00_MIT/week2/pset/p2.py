"""
    This module calculates the credit card balance after
    one year if a person only pays the minimum payment
    required by the credit card company each month.
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
    i = 1
    while balance_next_year(balance, annual_interest_rate, 10 * i) > 0:
        i += 1
    return i * 10
