import tempfile,unittest
from pathlib import Path
from table_reconcile import reconcile
class Tests(unittest.TestCase):
 def run_case(self,a,b,**kw):
  with tempfile.TemporaryDirectory() as d:
   l=Path(d,'l.csv');r=Path(d,'r.csv');l.write_text(a);r.write_text(b);return reconcile(l,r,['id'],**kw)
 def test_keyed_order_tolerance(self):
  x=self.run_case('id,total\n1,0.30\n2,7\n','id,total\n2,7\n1,0.31\n',tolerances={'total':'0.01'});self.assertEqual(x['changed'],[])
 def test_missing_changed_schema(self):
  x=self.run_case('id,a\n1,x\n2,y\n','id,a,b\n1,z,q\n3,v,s\n');self.assertEqual(x['left_only'],[['2']]);self.assertEqual(x['right_only'],[['3']]);self.assertEqual(x['schema']['right_only'],['b']);self.assertEqual(len(x['changed']),2)
 def test_duplicate_rejected(self):
  with self.assertRaisesRegex(ValueError,'duplicate key'):self.run_case('id,a\n1,x\n1,y\n','id,a\n1,z\n')
 def test_negative_tolerance_rejected(self):
  with self.assertRaises(ValueError):self.run_case('id,a\n1,3\n','id,a\n1,4\n',tolerances={'a':'-1'})
 def test_quoted_newline(self):
  x=self.run_case('id,a\n1,"hello\nworld"\n','id,a\n1,"hello\nworld"\n');self.assertEqual(x['changed'],[])
 def test_high_precision_boundary(self):
  x=self.run_case('id,total\n1,0\n','id,total\n1,1.00000000000000000000000000001\n',tolerances={'total':'1'});self.assertEqual(len(x['changed']),1)
 def test_equal_nonfinite_cells_rejected(self):
  with self.assertRaises(ValueError):self.run_case('id,total\n1,NaN\n','id,total\n1,NaN\n',tolerances={'total':'1'})
