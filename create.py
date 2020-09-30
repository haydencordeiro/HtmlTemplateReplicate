import pandas as pd
import json


def CreateFiles(values, TemplateFileName="template.html", outputFileName="test"):

    f = open(TemplateFileName)
    template = f.readlines()
    f.close()

    template = ''.join(template)
    lenD = (len(values[list(values.keys())[0]]))
    for i in range(lenD):
        temp = template
        for j, k in enumerate(values.keys()):
            # print('$${}$$'.format(k), values[k][i])
            temp = temp.replace('$${}$$'.format(k), str(values[k][i]))
            t = open(outputFileName+str(i)+".html", "w")
            t.write(temp)
            t.close()


def CreateDict():
    d = {}
    df = pd.read_excel('data.xlsx')
    json_value = df.to_dict('list')
    CreateFiles((json_value))


CreateDict()
