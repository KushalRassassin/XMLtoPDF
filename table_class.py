from create_table_fpdf2 import PDF


data = [
    ["First name", "Last name", "Age", "City",], # 'testing','size'],
    ["Jules", "Smith", "34", "San Juan",], # 'testing','size'],
    ["Mary", "Ramos", "45", "Orlando",], # 'testing','size'],
    ["Carlson", "Banks", "19", "Los Angeles",], # 'testing','size'],
    ["Lucas", "Cimon", "31", "Saint-Mahturin-sur-Loire",], # 'testing','size'],
]

data_as_dict = {"First name": ["Jules","Mary","Carlson","Lucas"],
                "Last name": ["Smith","Ramos","Banks","Cimon"],
                "Age": [34,'45','19','31']
            }


pdf = PDF()
pdf.add_page()
pdf.set_font("Times", size=10)

pdf.create_table(table_data = data_as_dict,title='',align_header='R', align_data='R', cell_width=[15,15,10,45,], x_start='C', emphasize_data=['45','Jules'], emphasize_style='BIU',emphasize_color=(255,0,0))
pdf.ln()


pdf.output('table_class.pdf')