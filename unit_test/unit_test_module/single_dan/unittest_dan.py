import unittest
from nltk import word_tokenize

def carré(x):
    """Élève au carré."""
    return x ** 2

def lowerize(txt):
    """Mettre en minuscule"""
    return txt.lower()

def capitalize(txt):
    # Mettre en majuscule
    return txt.upper()

def tokenize(txt):
    """Séparer les mots d'une phrase"""
    return txt.split()

class CarreTestCase(unittest.TestCase):
    """Classe testeur pour la fonction carrée."""

    test_values = ((2, 4), (0, 0), (-2, 4))
    test_sentences = (("Ok!", "ok!"), ("JeSuisLeMaitre","jesuislemaitre"), ("Do you need a special Tool?","do you need a special tool?"))
    test_capit = (("om", "OM"), ("Mignonne, allons voir si la rose", "MIGNONNE, ALLONS VOIR SI LA ROSE"))
    text = "La cigale ayant chanté tout l'été se trouva fort dépourvue quand la bise fut venue"
    tokenized = ['La', 'cigale', 'ayant', 'chanté', 'tout', "l'été", 'se', 'trouva', 'fort', 'dépourvue', 'quand', 'la', 'bise', 'fut', 'venue']

    def test_carré(self):
        """Teste les valeurs références."""
        for value, expected in self.test_values:
            self.assertEqual(carré(value), expected)
    
    def test_lower(self):
        """Teste les valeurs références."""
        for value, expected in self.test_sentences:
            self.assertEqual(lowerize(value), expected)
    def test_upper(self):
        """Teste les valeurs références."""
        for value, expected in self.test_capit:
            self.assertEqual(capitalize(value), expected)

    def test_tokenize(self):
        """Teste les valeurs références."""
        self.assertEqual(tokenize(self.text), word_tokenize(self.text))

if __name__ == '__main__':
    unittest.main()