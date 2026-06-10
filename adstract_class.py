from abc import ABC, abstractmethod

class PaymentSystem(ABC):

    @abstractmethod
    def process_payment(self):
        pass

class Visa(PaymentSystem):
    def process_payment(self):
        return "Оплата через Visa"
    

class Card(ABC):
    def _init_(self, payment_system):
        self.payment_system=payment_system

    @abstractmethod
    def pay(self):
        pass

class DebitCard(Card):
    def pay(self):
        print(f"Дебетовая карта: {self.payment_system.process_payment()}")

class CreditCard(Card):

    def pay(self):
        print(f"Кредитная карта: {self.payment_system.process_payment()}")