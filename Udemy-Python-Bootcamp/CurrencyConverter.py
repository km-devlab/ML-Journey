class LocalCurrencyConverter:
    def __init__(self):
        # Hardcoded conversion rates relative to 1 USD
        # You can easily adjust these values to update your local rates
        self.rates_to_usd = {
            "USD": 1.0,
            "INR": 83.50,  # 1 USD = 83.50 INR
            "SGD": 1.35,  # 1 USD = 1.35 SGD
            "EUR": 0.92,  # 1 USD = 0.92 EUR
            "GBP": 0.79,  # 1 USD = 0.79 GBP
            "CAD": 1.37,  # 1 USD = 1.37 CAD
            "AUD": 1.51,  # 1 USD = 1.51 AUD
            "JPY": 156.0  # 1 USD = 156.0 JPY
        }

    def convert(self, from_currency, to_currency, amount):
        # Check if both currencies exist in our local database
        if from_currency not in self.rates_to_usd:
            print(f"❌ Error: Currency '{from_currency}' is not supported locally.")
            return
        if to_currency not in self.rates_to_usd:
            print(f"❌ Error: Currency '{to_currency}' is not supported locally.")
            return

        # Step 1: Convert the source currency amount back to USD base
        amount_in_usd = amount / self.rates_to_usd[from_currency]

        # Step 2: Convert the USD base amount into the target currency
        final_amount = round(amount_in_usd * self.rates_to_usd[to_currency], 2)

        print(f"\n✨ Calculation Successful:")
        print(f"👉 {amount} {from_currency} = {final_amount} {to_currency}")


if __name__ == "__main__":
    converter = LocalCurrencyConverter()

    try:
        from_currency = input("From Currency (e.g., USD): ").strip().upper()
        to_currency = input("To Currency (e.g., INR): ").strip().upper()
        amount = float(input("Amount: "))

        print("Calculating rate locally...")
        converter.convert(from_currency, to_currency, amount)

    except ValueError:
        print("❌ Error: Please enter a valid number for the amount.")

