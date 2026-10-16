"""
CodeAlpha Python Internship - Task 2: Stock Portfolio Tracker
Calculates total investment value from hardcoded stock prices.
Concepts: dictionary, input/output, basic arithmetic, file handling
"""

import csv
from datetime import datetime

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125,
}


def show_available_stocks():
    print("\nAvailable stocks and prices:")
    print("-" * 28)
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<8} ${price}")
    print("-" * 28)


def get_portfolio():
    """Ask the user for stock names and quantities. Returns a dict."""
    portfolio = {}
    print("\nEnter your stocks. Type 'done' when finished.")

    while True:
        symbol = input("\nStock symbol (or 'done'): ").strip().upper()
        if symbol == "DONE":
            break
        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' is not available. Choose from: {', '.join(STOCK_PRICES)}")
            continue

        qty_text = input(f"Quantity of {symbol}: ").strip()
        if not qty_text.isdigit() or int(qty_text) <= 0:
            print("Please enter a positive whole number.")
            continue

        portfolio[symbol] = portfolio.get(symbol, 0) + int(qty_text)
        print(f"Added {qty_text} share(s) of {symbol}.")

    return portfolio


def calculate_total(portfolio):
    total = 0
    rows = []
    for symbol, qty in portfolio.items():
        value = STOCK_PRICES[symbol] * qty
        total += value
        rows.append((symbol, qty, STOCK_PRICES[symbol], value))
    return rows, total


def print_summary(rows, total):
    print("\n" + "=" * 50)
    print("            PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"{'Stock':<8}{'Qty':>6}{'Price':>10}{'Value':>14}")
    print("-" * 50)
    for symbol, qty, price, value in rows:
        print(f"{symbol:<8}{qty:>6}{'$' + str(price):>10}{'$' + str(value):>14}")
    print("-" * 50)
    print(f"{'TOTAL INVESTMENT':<24}{'$' + str(total):>26}")
    print("=" * 50)


def save_to_txt(rows, total, filename="portfolio.txt"):
    with open(filename, "w") as f:
        f.write(f"Portfolio Summary - {datetime.now():%Y-%m-%d %H:%M}\n")
        f.write("-" * 40 + "\n")
        for symbol, qty, price, value in rows:
            f.write(f"{symbol}: {qty} x ${price} = ${value}\n")
        f.write("-" * 40 + "\n")
        f.write(f"Total Investment: ${total}\n")
    print(f"Saved to {filename}")


def save_to_csv(rows, total, filename="portfolio.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        writer.writerows(rows)
        writer.writerow(["TOTAL", "", "", total])
    print(f"Saved to {filename}")


def main():
    print("=== STOCK PORTFOLIO TRACKER ===")
    show_available_stocks()

    portfolio = get_portfolio()
    if not portfolio:
        print("\nNo stocks entered. Exiting.")
        return

    rows, total = calculate_total(portfolio)
    print_summary(rows, total)

    choice = input("\nSave result? (txt / csv / both / no): ").strip().lower()
    if choice in ("txt", "both"):
        save_to_txt(rows, total)
    if choice in ("csv", "both"):
        save_to_csv(rows, total)


if __name__ == "__main__":
    main()
