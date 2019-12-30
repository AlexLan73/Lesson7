"""
LIGHT:
1) Вручную создать текстовый файл с данными (например, марка авто, модель авто, расход топлива, стоимость).
2) Создать doc шаблон, где будут использованы данные параметры.
3) Автоматически сгенерировать отчет о машине в формате doc (как в видео 7.2).
4) Создать csv файл с данными о машине.
5) Создать json файл с данными о машине. 
6) Замерить время генерации отчета (время выполнения пункта 3). 
В каждый файл пунктов 4 и 5 добавить параметр: время, затраченное на генерацию отчета.
"""
import datetime
import csv
import json
import timeit
from docx.shared import Cm
from docxtpl import DocxTemplate

def from_template(dmodel, template):
    template = DocxTemplate(template)
    context = dmodel

    template.render(context)
    
    template.save(dmodel['mark']+"_"+ dmodel['model'] \
       +"_"+str(datetime.datetime.now().date()) +'_report.docx')

def generate_report(dmodel):
    template = "PriceAuto.docx"
#    document=from_template(dmodel, template)

    template = DocxTemplate(template)
    context = dmodel

    template.render(context)
    
    template.save(dmodel['mark']+"_"+ dmodel['model'] \
       +"_"+str(datetime.datetime.now().date()) +'_report.docx')


if __name__ == "__main__":
    ls=[]
    with open('avto.txt') as f:
        for line in f:
            ls.append(line.replace('\n',"").split(','))

    with open('avto.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(ls)

    ls_json= json.dumps(ls)

    with open('avto.json', 'w', ) as f:
         f.write(ls_json)
  

    dmodel=dict(mark='bmw', model='x1', price=970000, 
    year=2014, mileage=49500, body='кроссовер', 
    kpp="автомат", fuel="бензин", volume=2.0, power=150.0)
    generate_report(dmodel)
    def generate_report1():
        generate_report(dmodel)

    xtime=timeit.timeit("generate_report1()", setup="from __main__ import generate_report1", number=1)
    sxtime=str(xtime)
    print(xtime)
    xls=[('time', sxtime)]

    with open('avto.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(xls)

    ls_jsonxls= json.dumps(xls)

    with open('avto.json', 'a', ) as f:
         f.write(ls_jsonxls)

i=1    

