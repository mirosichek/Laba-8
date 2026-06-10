from abc import ABC, abstractmethod


class PaymentSystem(ABC):

    @abstractmethod
    def process_payment(self):
        pass


class Visa(PaymentSystem):

    def process_payment(self):
        return "Оплата через Visa"


class MasterCard(PaymentSystem):

    def process_payment(self):
        return "Оплата через MasterCard"


class Mir(PaymentSystem):

    def process_payment(self):
        return "Оплата через Мир"