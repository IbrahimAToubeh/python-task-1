from .mixins import AuditMixin

class Wallet(AuditMixin):
    def __init__(self, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self._balance = initial_balance

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        self.log_action("Deposit", f"Deposited {amount:.2f}. New balance: {self._balance:.2f}")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount
        self.log_action("Withdrawal", f"Withdrew {amount:.2f}. New balance: {self._balance:.2f}")

    def transfer(self, recipient_wallet: 'Wallet', amount: float):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        self.withdraw(amount)
        recipient_wallet.deposit(amount)
        self.log_action("Transfer", f"Transferred {amount:.2f} to wallet.")
