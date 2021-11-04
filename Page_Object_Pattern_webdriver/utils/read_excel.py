import xlrd

from Page_Object_Pattern.utils.search_data import SearchData


class ExcelReader:

    @staticmethod
    def get_data():
        wb = xlrd.open_workbook(r"..\utils\Zeszyt1.xlsx")
        sheet = wb.sheet_by_index(0)
        data = []
        for i in range (1, sheet.nrows):
            search_data = SearchData(sheet.cell(i,0).value, sheet.cell(i,1).value)
            data.append(search_data)
        return data


