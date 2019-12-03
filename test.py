# Define Book price details,min book charges and minimum Rental Days for each book
book_charges = {"regular": 1.5, "fiction": 3, "novels": 1.5}
min_book_charges = {"regular": 2, "fiction": 0, "novels": 4.5}
min_rent_days = {"regular": 2, "fiction": 0, "novels": 3}
books_cat = ['Regular', 'Novels', 'fiction']
# print("----Select count of books for each category----")

'''
This class helps to initialize user provided book details and rent duration
and calculates total amount customer has to pay for rent
'''


class BookStoreInfo:

    def __init__(self, regular_books, novels_books, fiction_books, regular_days, novels_days, fiction_days):
        self.regular_books = regular_books
        self.novels_books = novels_books
        self.fiction_books = fiction_books
        self.regular_days = regular_days
        self.novels_days = novels_days
        self.fiction_days = fiction_days
        self.total_rent=0

    def get_data(self):
        rent_books_data = []
        rent_books_data.append(("regular", int(self.regular_books), int(self.regular_days)))
        rent_books_data.append(("fiction", int(self.fiction_books), int(self.fiction_days)))
        rent_books_data.append(("novels", int(self.novels_books), int(self.novels_days)))
        return rent_books_data

    def rent_calc(self):
        rent_books = self.get_data()
        total_rent = 0
        for row in rent_books:
            if row[0] in book_charges:
                if row[2] < min_rent_days[row[0]]:
                    partial_rent = row[1] * min_book_charges[row[0]] * row[2]
                    total_rent = total_rent + partial_rent
                else:
                    if row[0] == "regular":
                        partial_rent = row[1] * 2 + row[1] * (row[2] - 2) * book_charges[row[0]]
                        total_rent = total_rent + partial_rent
                    else:
                        partial_rent = row[1] * row[2] * book_charges[row[0]]
                        total_rent = total_rent + partial_rent
        print("Regular Books and Rent Days:", int(self.regular_books), "-", int(self.regular_days))
        print("Fiction Books and Rent Days:", int(self.fiction_books), "-", int(self.fiction_days))
        print("Novel Books and Rent Days  :", int(self.novels_books),"-", int(self.novels_days))
        print("----------------------------------------")
        return total_rent

