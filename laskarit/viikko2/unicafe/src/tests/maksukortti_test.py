import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)
    
    def test_saldo_oikein_str_metodissa(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_saldo_euroina_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_kortin_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(self.maksukortti.saldo, 1500)
    
    def test_saldo_vähenee_kun_rahaa_otetaan(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(self.maksukortti.saldo, 800)
    
    def test_saldo_ei_vähene_kun_rahaa_otetaan_liikaa(self):
        self.maksukortti.ota_rahaa(1200)
        self.assertEqual(self.maksukortti.saldo, 1000)
    
    def test_ota_rahaa_palauttaa_true_kun_rahaa_on_tarpeeksi(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)
