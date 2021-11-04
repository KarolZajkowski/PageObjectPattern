import xlrd
from page_object_pattern.utils.search_data import SearchData


class ExcelReader:

    @staticmethod
    def get_data():
        wb = xlrd.open_workbook(r"..\utils\phone_number.xlsx")
        sheet = wb.sheet_by_index(0)
        data = []
        for i in range(1, sheet.nrows):
            search_data = SearchData(sheet.cell(i, 0).value, sheet.cell(i, 1).value, sheet.cell(i, 2).value)
            data.append(search_data)
        return data
