from typing import AsyncContextManager
import zadanie_3

class TestKoren:
    def test_discriminant(self):
        assert zadanie_3.discriminant(2,4,1) == 8
    
    def test_two_koren(self):
        assert zadanie_3.koren(4, 5, 1) == (-1.0, -0.25)

    def test_one_koren(self):
        assert zadanie_3.one_koren(4,5) == -0.625
    def test_zero(self):
        assert zadanie_3.zero_koren(4,2,2) < 0
    