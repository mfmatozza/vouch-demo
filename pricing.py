"""Order pricing for a small online shop."""


def subtotal(items):
    """items: list of (unit_price, quantity)."""
    return round(sum(price * qty for price, qty in items), 2)


def discount(amount, code):
    """Percentage discount codes."""
    rates = {"WELCOME10": 0.10, "VIP20": 0.20, "STUDENT15": 0.15}
    return round(amount * (1 - rates.get(code, 0)), 2)


def shipping(amount):
    """Free shipping from 50 EUR, otherwise a flat 4.90."""
    return 0.0 if amount >= 50 else 4.90
