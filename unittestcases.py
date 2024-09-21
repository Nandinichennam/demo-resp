import unittest 
from multiply import multiplication
class multiplyTestcase(unittest,Testcase):
  def test_1(self):
    result=multiplication(3,4)
    self.assertEqual(result,12)
    def tetst_2(self):
      result=multiplication(-3,4)
      self.assertEqualresult(result,12)
      if__name_=='__main__':
      unittest.main()
    def test_3(self):
      result=multiplication(-3,-4)
      self.assertEqual(result,12)
      def test_4(self):
        result=multiplication(-3,4)
        self.assertEqual(result,-12)
        if__name_=='__main__':
        unittest.main()
