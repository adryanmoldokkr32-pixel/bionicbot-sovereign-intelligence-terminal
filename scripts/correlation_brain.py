import numpy as np

class CorrelationBrain:
    """Pillar 12: Cross-Asset Mathematical Logic"""
    
    def calculate_divergence(self, dxy_move, gold_move):
        """
        Standard: DXY down -> Gold up.
        Divergence: DXY down -> Gold stable/down (Institutional accumulation detected)
        """
        if dxy_move < 0 and gold_move <= 0:
            return "INSTITUTIONAL_ABSORPTION_DETECTED: Whale keeping price down"
        return "NORMAL_CORRELATION"

    def get_market_vibe(self, vix_index, fear_greed_score):
        """Calculates the psychological state of the market"""
        if vix_index > 30 and fear_greed_score < 20:
            return "MAXIMUM_BLOOD_IN_STREETS: High probability reversal"
        return "STABLE_FLOW"