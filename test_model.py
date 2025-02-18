import unittest
from model_training import train_model
from data_preprocessing import load_and_preprocess_data

class TestModel(unittest.TestCase):
    def test_model_training(self):
        features, target = load_and_preprocess_data('market_data.csv')
        self.assertIsNotNone(features)
        self.assertIsNotNone(target)
        train_model(features, target)

if __name__ == '__main__':
    unittest.main() 