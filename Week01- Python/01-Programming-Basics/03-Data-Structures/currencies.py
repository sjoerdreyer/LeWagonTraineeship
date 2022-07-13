# pylint: disable=missing-docstring


RATES = {
    'USDEUR': 0.85,
    'GBPEUR': 1.13,
    'CHFEUR': 0.86,
    'EURGBP': 0.885,
}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """
    key = f'{amount[1]}{currency}'
    if key not in RATES:
        return None
    conversion = round(RATES[key]*amount[0], 0)
    return conversion
