import tempfile,json
from pathlib import Path
from table_reconcile import reconcile
with tempfile.TemporaryDirectory() as d:
 a=Path(d,'old.csv');b=Path(d,'new.csv');a.write_text('id,total\nA,10.00\nB,7.00\n');b.write_text('id,total\nA,10.01\nC,8.00\n');print(json.dumps(reconcile(a,b,['id'],{'total':'0.01'}),indent=2))
