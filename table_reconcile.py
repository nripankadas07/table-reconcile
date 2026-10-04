import argparse,csv,json
from decimal import Decimal,InvalidOperation
from pathlib import Path
from fractions import Fraction
def read(path,keys):
    with Path(path).open(newline='',encoding='utf-8-sig') as f:
        r=csv.DictReader(f);fields=r.fieldnames
        if not fields or len(fields)!=len(set(fields)): raise ValueError('missing or duplicate CSV headers')
        if not all(k in fields for k in keys): raise ValueError('key column missing')
        rows={}
        for number,row in enumerate(r,2):
            if None in row or any(v is None for v in row.values()): raise ValueError(f'malformed CSV row {number}')
            key=tuple(row[k] for k in keys)
            if any(not k for k in key): raise ValueError(f'empty key at row {number}')
            if key in rows: raise ValueError(f'duplicate key at row {number}: {key!r}')
            rows[key]=row
        return fields,rows
def reconcile(left,right,keys,tolerances=None,ignore=()):
    if not keys or len(keys)!=len(set(keys)):raise ValueError('provide distinct key columns')
    try: tolerances={k:Decimal(str(v)) for k,v in (tolerances or {}).items()}
    except InvalidOperation as e: raise ValueError('invalid decimal tolerance') from e
    if any(not v.is_finite() or v<0 or len(v.as_tuple().digits)>1000 or abs(v.as_tuple().exponent)>1000 for v in tolerances.values()):raise ValueError('tolerances must be finite, nonnegative, and within 1000 digits/exponent')
    lf,l=read(left,keys);rf,r=read(right,keys);fields=sorted((set(lf)|set(rf))-set(keys)-set(ignore))
    if not set(tolerances)<=set(fields):raise ValueError('tolerance column missing or excluded')
    changes=[]
    for key in sorted(set(l)&set(r)):
        for field in fields:
            a=l[key].get(field);b=r[key].get(field);same=a==b
            if field in tolerances and a is not None and b is not None:
                try:
                    x,y=Decimal(a),Decimal(b)
                    if any(not v.is_finite() or len(v.as_tuple().digits)>1000 or abs(v.as_tuple().exponent)>1000 for v in (x,y)):raise ValueError('numeric cells must be finite and within 1000 digits/exponent')
                    same=abs(Fraction(x)-Fraction(y))<=Fraction(tolerances[field])
                except InvalidOperation as e:raise ValueError(f'nonnumeric tolerance cell in {field}') from e
            if not same:changes.append({'key':list(key),'column':field,'left':a,'right':b})
    return {'left_only':[list(k) for k in sorted(set(l)-set(r))], 'right_only':[list(k) for k in sorted(set(r)-set(l))], 'changed':changes,'schema':{'left_only':sorted(set(lf)-set(rf)),'right_only':sorted(set(rf)-set(lf))},'matched_keys':len(set(l)&set(r))}
def main():
    p=argparse.ArgumentParser();p.add_argument('left');p.add_argument('right');p.add_argument('--key',action='append',required=True);p.add_argument('--ignore',action='append',default=[]);p.add_argument('--tolerance',action='append',default=[]);a=p.parse_args()
    try:
        tol=dict(x.split('=',1) for x in a.tolerance);result=reconcile(a.left,a.right,a.key,tol,a.ignore)
    except (ValueError,OSError) as e:p.exit(2,str(e)+'\n')
    print(json.dumps(result,indent=2));return int(bool(result['changed'] or result['left_only'] or result['right_only'] or any(result['schema'].values())))
if __name__=='__main__':raise SystemExit(main())
