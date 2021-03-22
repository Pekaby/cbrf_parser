from bs4 import BeautifulSoup

class pa:
    def __init__(self, html):
        self.soup_main = BeautifulSoup(html, 'html.parser')
        table_main = BeautifulSoup(str(self.soup_main.findAll('table', class_='data')), 'html.parser') # Main table soup
        self.data_table = BeautifulSoup(str(table_main.findAll('tr')), 'html.parser') # table data with <tr></tr>

        self.thead = BeautifulSoup(str(self.data_table.findAll('th')), 'html.parser') # thead of table

        self.data = BeautifulSoup(str(self.data_table.findAll('td')), 'html.parser') # td table with normal data

    def __logic(self, search):
        # Getting thead 
        self.thead = self.thead.text.replace('[', '')
        self.thead = self.thead.replace(']', '')
        self.thead = self.thead.rsplit(', ')
        
        self.__SEARCH = 4
        self.__NAME = 1

        # Deleting thead from table tada
        self.data = self.data.text.replace('[', '')
        self.data = self.data.replace(']', '')
        self.data = self.data.rsplit(', ')
        return self.__finde_course(search)

    def __finde_course(self, search):
        count = 0
        for x in self.data:
            if x == search:
                self.course = self.data[int(self.__SEARCH) + int(count)]
                self.name = self.data[int(self.__NAME) + int(count)]
                break
            count = count + 1       
        return self.course

    def find_by_code(self, code):
        self.__logic(code)

    def get_course(self):
        return self.course
    
    def get_name(self):
        return self.name
