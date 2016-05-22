import xlsxwriter

class Save_data():

    def save(self, list_obj):
        workbook = xlsxwriter.Workbook('demo.xlsx')
        worksheet = workbook.add_worksheet()

        # Start from the first cell. Rows and columns are zero indexed.
        row = 0
        col = 0

        titles = ['headline', 'date', 'imageURL', 'content', 'author' ]

        for x in titles:
            worksheet.write(row, col, x)
            # row += 1
            col += 1


        row = 1
        for x in list_obj:

            col = 0
            for key, values in x.items():
                # print values
                worksheet.write(row, col, values)

                col += 1
            row += 1
        workbook.close()




