import unittest

from ilike import (
    clamp_probability,
    complement,
    odds_to_probability,
    probability_to_odds,
)


class TestPublicApi(unittest.TestCase):
    def test_top_level_exports(self):
        self.assertEqual(clamp_probability(2.0), 1.0)
        self.assertEqual(clamp_probability(-0.5), 0.0)
        self.assertAlmostEqual(complement(0.3), 0.7)
        self.assertAlmostEqual(probability_to_odds(0.75), 3.0)
        self.assertAlmostEqual(odds_to_probability(3.0), 0.75)

    def test_module_organization_still_available(self):
        from ilike.odds import odds_to_probability as module_odds_to_probability
        from ilike.probability import complement as module_complement

        self.assertAlmostEqual(module_complement(0.2), 0.8)
        self.assertAlmostEqual(module_odds_to_probability(1.0), 0.5)


if __name__ == "__main__":
    unittest.main()
