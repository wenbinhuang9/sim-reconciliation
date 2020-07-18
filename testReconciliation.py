import unittest
import reconciliaton as recon 

## add todo 







## todo intergration test
## todo think about the interface???
## how about using bit data ???
class TestRecon(unittest.TestCase):
    def test_where(self):
        recon.where("order.csv", "$2 >100 && $3== 1")

    def test_selection(self):
        recon.selection("out_order.csv", "amt", "|")

    def test_transform(self):
        recon.transform("out_order.csv", "$2 = $2 * 100;", "|")

    def test_merge(self):
        recon.merge("order.csv", "out_order.csv")

    def test_diff(self):
        recon.diff("order.csv", "out_order.csv")

    def test_rename(self):
        recon.rename("out_order.csv", "orderid|amount")
if __name__== '__main__':
    unittest.main()
