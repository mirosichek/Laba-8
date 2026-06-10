from abc import ABC, abstractmethod


class Card(ABC):

    def __init__(self, payment_system):
        self.payment_system = payment_system

    @abstractmethod
    def pay(self):
        pass


class DebitCard(Card):

    def pay(self):
        print(f"Дебетовая карта: {self.payment_system.process_payment()}")


class CreditCard(Card):

    def pay(self):
        print(f"Кредитная карта: {self.payment_system.process_payment()}")