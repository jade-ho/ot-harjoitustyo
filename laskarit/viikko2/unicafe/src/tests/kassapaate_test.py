import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)
    
    def test_edullisen_lounaan_osto_kateisella_toimii(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.40)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_maukkaan_lounaan_osto_kateisella_toimii(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.00)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_edullisen_lounaan_osto_kateisella_ei_toimi(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_maukkaan_lounaan_osto_kateisella_ei_toimi(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_edullisen_lounaan_osto_kortilla_toimii(self):
        from maksukortti import Maksukortti
        kortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), True)
        self.assertEqual(kortti.saldo, 760)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_maukkaan_lounaan_osto_kortilla_toimii(self):
        from maksukortti import Maksukortti
        kortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), True)
        self.assertEqual(kortti.saldo, 600)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_edullisen_lounaan_osto_kortilla_ei_toimi(self):
        from maksukortti import Maksukortti
        kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_maukkaan_lounaan_osto_kortilla_ei_toimi(self):
        from maksukortti import Maksukortti
        kortti = Maksukortti(300)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
        self.assertEqual(kortti.saldo, 300)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_rahan_lataaminen_kortille_toimii(self):
        from maksukortti import Maksukortti
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, 500)
        self.assertEqual(kortti.saldo, 1500)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1005.00)
    
    def test_rahan_lataaminen_kortille_ei_toimi(self):
        from maksukortti import Maksukortti
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, -500)
        self.assertEqual(kortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)
    