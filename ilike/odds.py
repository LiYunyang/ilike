"""Odds/probability conversion helpers."""


def probability_to_odds(probability: float) -> float:
    """Convert probability p into odds p / (1 - p)."""
    if not 0.0 <= probability < 1.0:
        raise ValueError("probability must be in [0.0, 1.0)")
    return probability / (1.0 - probability)


def odds_to_probability(odds: float) -> float:
    """Convert odds into probability odds / (1 + odds)."""
    if odds < 0.0:
        raise ValueError("odds must be non-negative")
    return odds / (1.0 + odds)
