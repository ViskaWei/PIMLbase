import numpy as np
from unittest import TestCase
from base.interface.surface.IO.baseloader import H5pyLoader, ZarrLoader, NpLoader, PickleLoader

PATH = "/test/testdata/bosz_5000_test.h5"

class TestBaseLoader(TestCase):

    def test_H5pyLoader(self):
        loader = H5pyLoader()
        DArgs = loader.load_dict_args(PATH)
        self.assertIsNotNone(DArgs)
        self.assertEqual(DArgs["flux"].shape, (120,1178))
        self.assertEqual(DArgs["wave"].shape, (1178,))
        self.assertIsNone(np.testing.assert_array_equal(DArgs["pdx"][0], [6, 8, 4, 3, 1]))

        
        
