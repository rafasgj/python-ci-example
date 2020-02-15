"""Test cards module."""

from pytest import fixture

import cards


@fixture
def configured_dealer():
    """Initialize a Dealer to use on tests."""
    return cards.Dealer()


@fixture
def valid_cards():
    """Configure the valid cards."""
    return ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def test_dealer(configured_dealer, valid_cards):
    """Test the Dealer class."""
    hand = configured_dealer.hand
    assert [c for c in hand if c not in valid_cards] == []
