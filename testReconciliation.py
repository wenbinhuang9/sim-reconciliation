import unittest
import reconciliaton as recon 

## todo finish the test job here 
class TestRecon(unittest.TestCase):

    def test_filterRows(self):
        recon.filterRows("order.csv", "$2 >50 && $3== 1")

    def test_filterColumns(self):
        recon.filterCols("out_order.csv", ["amt"])


if __name__== '__main__':
    unittest.main()