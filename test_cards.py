from cards import DebitCard, CreditCard
from payment_system import Visa, MasterCard
import pytest

def test_debit_card_with_visa(capsys):
    card = DebitCard(Visa())

    card.pay()

    captured = capsys.readouterr()
    assert captured.out.strip() == "Дебетовая карта: Оплата через Visa"

def test_test_credit_card_with_mastercard(capsys):
    card=CreditCard(MasterCard())

    card.pay()

    captured = capsys.readouterr()
    assert captured.out.strip() == "Кредитная карта: Оплата через MasterCard"

@pytest.mark.xfail
def test_test_credit_card_with_mastercard(capsys):
    card=CreditCard(MasterCard())

    card.pay()

    captured = capsys.readouterr()
    assert captured.out.strip() == "Кредитная карта: лата через MasterCard"

