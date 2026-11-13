import json,sys
d=json.load(open(sys.argv[1]))
cols=['total','hombre','mujer','edad_18_29','edad_30_44','edad_45_mas','nse_a','nse_b','nse_c','nse_d','nse_e','callao','lima_norte','lima_centro','lima_sur','lima_este']
rows=[]
for q in d['questions']:
  for r in q['rows']:
    o={'pregunta':q['id'],'tema':r.get('item') or '','respuesta':r['label']}
    for c,v in zip(cols,r['v']): o[c]=round(v*100,1)
    rows.append(o)
code=open(sys.argv[0]).read()
meta=[{'label':'Fuente','value':'TablasEncuestaLCV2025.xlsx, hoja "Tablas" (Lima Cómo Vamos, encuesta 2025)'},
      {'label':'Unidad','value':'Porcentaje de entrevistados (0–100). Base: total de entrevistas, n = 1140.'},
      {'label':'rows.py','value':code,'type':'code','lang':'python'}]
json.dump({'rows':rows,'meta':meta},open(sys.argv[2],'w'),ensure_ascii=False,separators=(',',':'))
secc={'P2':'Ciudad','P3':'Ciudad','P4':'Ciudad','P5':'Seguridad','P6':'Seguridad','P7':'Seguridad','P8':'Movilidad','P9':'Movilidad','P10':'Movilidad','P11':'Movilidad','P12':'Movilidad','P16':'Movilidad','P17':'Ambiente','P18':'Ambiente','P22':'Vivienda y espacio público','P23':'Vivienda y espacio público','P24':'Vivienda y espacio público','P25':'Vivienda y espacio público'}
pq=[{'pregunta':q['id'],'seccion':secc[q['id']],'texto':q['text'],'tipo':'Escala por tema' if q['type']=='grid' else 'Respuesta única o múltiple','base':q.get('base','')} for q in d['questions']]
json.dump({'rows':pq,'meta':[{'label':'Ficha técnica','value':d['ficha']}]},open(sys.argv[3],'w'),ensure_ascii=False,separators=(',',':'))
print(len(rows))
