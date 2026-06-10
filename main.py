from cards import DebitCard, CreditCard
from payment_system import Visa, MasterCard, Mir


def main():
    card1 = DebitCard(Visa())
    card2 = CreditCard(MasterCard())
    card3 = DebitCard(Mir())

    card1.pay()
    card2.pay()
    card3.pay()


if __name__ == "__main__":
    main()