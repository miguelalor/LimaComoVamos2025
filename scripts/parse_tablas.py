import openpyxl, json, re, sys
wb=openpyxl.load_workbook(sys.argv[1],data_only=True)
ws=wb['Tablas']
SEG=['Total','Hombre','Mujer','18/29','30/44','45/+','A','B','C','D','E','Callao','Lima Norte','Lima Centro','Lima Sur','Lima Este']
qs=[];cur=None;r=2
while r<=ws.max_row:
  a=ws.cell(r,1).value
  if isinstance(a,str) and re.match(r'\s*P\d+\.',a):
    m=re.match(r'\s*(P\d+)\.\s*(.*)',a,re.S)
    text=re.sub(r'\s+',' ',m.group(2)).strip()
    grid = ws.cell(r+1,3).value==2025
    cur={'id':m.group(1),'text':text,'type':'grid' if grid else 'simple','rows':[]}
    qs.append(cur); r+=3; item=None; continue
  if cur and isinstance(a,str) and 'Total' in a and 'BASE' in a:
    cur['base']=re.sub(r'\s+',' ',a).strip(); cur=None; r+=1; continue
  if cur:
    if cur['type']=='simple':
      if a is not None:
        vals=[ws.cell(r,c).value for c in range(2,18)]
        cur['rows'].append({'label':re.sub(r'\s+',' ',str(a)).strip(),'v':[round(float(x or 0),4) for x in vals]})
    else:
      if a is not None: item=re.sub(r'\s+',' ',str(a)).strip()
      b=ws.cell(r,2).value
      if b is not None:
        vals=[ws.cell(r,c).value for c in range(3,19)]
        cur['rows'].append({'item':item,'label':re.sub(r'\s+',' ',str(b)).strip(),'v':[round(float(x or 0),4) for x in vals]})
  r+=1
intro=ws['A1'].value
json.dump({'segments':SEG,'ficha':intro,'questions':qs},open(sys.argv[2],'w'),ensure_ascii=False,indent=0)
for q in qs: print(q['id'],q['type'],len(q['rows']),q['text'][:160])
