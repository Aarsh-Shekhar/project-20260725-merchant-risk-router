import unittest

from merchant_risk_router.models import Record
from merchant_risk_router.scoring import score_record


class DepthCheck23(unittest.TestCase):
    def test_023_data_quality_guardrail(self):
        record = Record(id="merchant-023", exposure=60389, signal=0.579, urgency=8)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
