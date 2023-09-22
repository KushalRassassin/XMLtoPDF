import xml.etree.ElementTree as ET
from fpdf import FPDF
from create_table import PDF

mytree = ET.parse('DD_XML.xml')
myroot = mytree.getroot()
study = myroot[0]
metadata = study[2]
item = []

#print(metadata[0][0][0].text)
#pdf.write(4, metadata[0][0][0].text)
#for i in range(2, len(metadata)-1):
 #   item = metadata[i]
  #  print(item[1][0].text)
   # print(item[0][0].text)
x = metadata[0][0][0].text
result_list = []
result_list.append((x,""))
for i in range(2, len(metadata) - 1):
    item = metadata[i]
    key = item[1][0].text
    value = item[0][0].text
    result_list.append((key,value))

print(result_list)


print(x)
pdf = PDF()
pdf.add_page()
pdf.set_font("Times", size=10)

pdf.create_table(table_data = result_list ,title='Form DD - Implementation Options: HorizontalGeneric',align_header='C', align_data='L', cell_width='even', x_start='C', emphasize_data=['45','Jules'], emphasize_style='BIU',emphasize_color=(255,0,0))
pdf.output("file.pdf")
