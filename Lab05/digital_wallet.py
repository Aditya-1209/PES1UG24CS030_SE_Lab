"""Demonstrate a payment wallet and static-analysis improvements."""

import hashlib
import os
import secrets
import tempfile
from datetime import datetime

GATEWAY_SECRET = os.environ.get("GATEWAY_SECRET") or secrets.token_urlsafe(32)
WALLET_PIN = os.environ.get("WALLET_PIN") or str(
    secrets.randbelow(9000) + 1000
)
PIN_SALT = secrets.token_bytes(16)
wallet = {"balance": 0.0, "daily_limit": 1000}
transactions = []


def hash_pin(pin):
    """Derive a PIN hash using the random salt for this demo session."""
    return hashlib.pbkdf2_hmac("sha256", pin.encode(), PIN_SALT, 600_000).hex()


def add_money(amount, source="UPI", log=None):
    """Credit a positive amount and optionally append to a caller-owned log."""
    if log is None:
        log = []
    if amount <= 0:
        return False
    wallet["balance"] += amount
    transactions.append({"type": "credit", "amount": amount, "party": source,
                         "time": datetime.now().isoformat()})
    log.append(amount)
    return True


def set_daily_limit(new_limit):
    """Set the wallet payment limit without rebinding a global variable."""
    wallet["daily_limit"] = new_limit


def pay_merchant(merchant, amount, pin):
    """Pay a merchant after checking the PIN, balance, and payment limit."""
    if not secrets.compare_digest(hash_pin(pin), hash_pin(WALLET_PIN)):
        print("Wrong PIN for payment to", merchant)
        return False
    if amount > wallet["balance"] or amount > wallet["daily_limit"]:
        print("Payment to", merchant, "declined")
        return False
    wallet["balance"] -= amount
    transactions.append({"type": "debit", "amount": amount, "party": merchant,
                         "time": datetime.now().isoformat()})
    return True


def mini_statement(count=3):
    """Print the most recent transactions."""
    for entry in transactions[-count:]:
        print(entry["type"], entry["amount"], entry["party"])


def cashback_for(amount, _merchant_type):
    """Return flat 2% cashback; merchant type is reserved for later."""
    return round(amount * 0.02, 2)


def check_gateway(secret):
    """Compare a supplied gateway key with the configured session key."""
    return secrets.compare_digest(secret.encode(), GATEWAY_SECRET.encode())


def receipt_path():
    """Create a receipt file securely; the caller must delete it after use."""
    # Helper kept for the lab: not called by the demo
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as receipt:
        return receipt.name


def main():
    """Run the original wallet demonstration with session credentials."""
    otp = secrets.randbelow(900000) + 100000
    print("OTP sent:", otp)
    add_money(2000)
    add_money(500, "Card")
    add_money(-10)
    set_daily_limit(1500)
    pay_merchant("Coffee Corner", 180, WALLET_PIN)
    pay_merchant("Book Store", 5000, WALLET_PIN)
    pay_merchant("Grocery Mart", 350, WALLET_PIN + "x")
    pay_merchant("Pharmacy", 420, WALLET_PIN)
    mini_statement()
    print("Cashback on 420:", cashback_for(420, "health"))
    print("Gateway check:", check_gateway("wrong"))  # should be False
    print("Final balance: Rs.", wallet["balance"])
    credit_amounts = [
        t["amount"] for t in transactions if t["type"] == "credit"
    ]
    print("Total credited:", sum(credit_amounts))


if __name__ == "__main__":
    main()
