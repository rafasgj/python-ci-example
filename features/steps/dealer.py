"""Steps for the Dealer feature."""

from behave import given, when, then  # pylint: disable=no-name-in-module

from src.test import Dealer


@given('a dealer')
def _given_a_dealer(context):
    context.dealer = Dealer()


@when('the round starts')
def _when_the_round_starts(context):
    context.dealer.new_round()


@then('the dealer gives itself two cards')
def _then_dealer_gives_itself_two_cards(context):
    assert len(context.dealer.hand) == 2
