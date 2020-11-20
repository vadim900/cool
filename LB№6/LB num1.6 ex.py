import pandas as pd
book1name = "Тигролови"; book1author = "Іван Багряний"; book1ganre = "пригодницький роман"; book1year = "1946";
book2name = "Майстер корабля"; book2author = "Юрій Яновський"; book2ganre = "автобіографічний роман"; book2year = "1928";
book3name = "Ковчег часу"; book3author = "Марцін Щигельський"; book3ganre = "Дитяча фантастика"; book3year = "2016";
book4name = "Пригоди Тома Соєра"; book4author = "Марк Твен"; book4ganre = "пригодницький роман"; book4year = "1876";
class Str():
    def __init__(self, string):
        self.string = string
    def repeat(self, s):
        assert len(s) >= 4
        step = len(s)
        splitted = [self.string[i:i+step] for i in range(0, len(self.string), step)]
        for i in splitted:
            if s != i:
                return False
            return True
    def pal(self):
        return self.string.lower() == self.string.lower()[::-1]
class Liblary:
    def __init__(self):
        self.lib = pd.DataFrame(columns=['Назва','Автор','Жанр','Рік'])
    def __str__(self):
        return str(self.lib)
    def show(self, index): 
        return self.lib.loc[index]
    def add(self, Назва, Автор, Жанр, Рік):
        self.lib.loc[len(self.lib)] = [Назва, Автор, Жанр, Рік]
    def dell(self, назва):
        index = self.lib.loc[self.lib['Name'] == назва].index
        self.lib = self.lib.drop(index).reset_index(drop=True)
    def sort(self, by, column):
        return self.lib.loc[self.lib[column] == by]
Library = Liblary()
print("Всі книги")
Library.add("","","","")
Library.add(book1name, book1author, book1ganre, book1year)
Library.add(book2name, book2author, book2ganre, book2year)
Library.add(book3name, book3author, book3ganre, book3year)
Library.add(book4name, book4author, book4ganre, book4year)
print(Library)
print("---"+20); print("Жанр: пригодницький роман");print(Library.sort("пригодницький роман","Жанр"))
print("---"+20); print("Автор: Іван Багряний");print(Library.sort("Іван Багряний","Автор"))
print("---"+20); print("Рік видання: 1946");print(Library.sort("1946","Рік"))
