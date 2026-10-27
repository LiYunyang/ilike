"""Probability-related helpers."""


def clamp_probability(value: float) -> float:
    """Clamp a numeric value into the inclusive [0.0, 1.0] probability range."""
    return min(1.0, max(0.0, value))


def complement(probability: float) -> float:
    """Return the complementary probability (1 - p)."""
    return 1.0 - probability
