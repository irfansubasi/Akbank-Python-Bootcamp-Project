# Library Management System

class Library:
    def __init__(self):
        # Dosyayı aç ve dosya nesnesini self.file'a ata
        self.file = open("books.txt", "a+", encoding="utf-8")

    def __del__(self):
        # Nesne yok edildiğinde, dosyayı kapat -- destructor
        self.file.close()

    def list_books(self):
        # Dosyanın başına git
        self.file.seek(0)
        # Dosyadaki satırları oku ve bir listede sakla
        lines = self.file.read().splitlines()
        newBookList = []
        # Her satırı parçala ve kitap bilgilerini yeni bir listede sakla
        for line in lines:
            book_info = line.split(",")
            title = book_info[0].strip()
            author = book_info[1].strip()
            publish_year = book_info[2].strip()
            page_num = book_info[3].strip()
            newBookList.append([title, author, publish_year, page_num])
        # Kitapların çıktısını al
        for book in newBookList:
            print(f"Book: {book[0]}, Author:{book[1]}")

    def add_book(self):
        # Kullanıcıdan kitap bilgilerini al
        title = input("Title: ").strip().title()
        author = input("Author: ").strip().title()
        # Kullanıcıdan yayın yılı ve sayfa numarası alırken kullanıcı doğru formatta(int) bir girdi girene kadar döngü devam eder
        while True:
            try:
                publish_year = int(input("Release Year: ").strip())
                break
            except ValueError:
                print("Please enter a valid integer for the release year.")

        while True:
            try:
                page_num = int(input("Page Number: ").strip())
                break
            except ValueError:
                print("Please enter a valid integer for the page number.")
        # Kitap bilgilerini dosyaya ekle
        book_info = f"{title},{author},{publish_year},{page_num}\n"
        self.file.write(book_info)
        # Dosyanın başına git ve kullanıcıya kitabın başarıyla eklendiğini bildir
        self.file.seek(0)
        print("Book added successfully.")

    def remove_book(self):
        # Kaldırılacak kitabın adını kullanıcıdan al
        title_to_remove = input("Enter the title of the book to remove: ").strip().title()

        print(title_to_remove)
        self.file.seek(0)
        lines = self.file.read().splitlines()
        book_list = []

        # Dosyadaki her satırı oku ve kitapları bir listede sakla
        for line in lines:
            book_info = line.split(",")
            title = book_info[0].strip().title()
            author = book_info[1].strip().title()
            publish_year = book_info[2].strip()
            page_num = book_info[3].strip()
            book_list.append([title, author, publish_year, page_num])

        index_to_remove = None
        # Kullanıcının girdiği kitabı listede bul
        for index, book in enumerate(book_list):
            if book[0] == title_to_remove:
                index_to_remove = index
                break

        # Kitap listede bulunamazsa kullanıcıya bilgi ver ve fonksiyondan çık
        if index_to_remove is None:
            print("Book not found.")
            return

        # Kitabı listeden kaldır
        removed_book = book_list.pop(index_to_remove)
        # Dosyanın içeriğini sil
        self.file.seek(0)
        self.file.truncate()

        # Güncellenmiş kitap listesini dosyaya yaz
        for book in book_list:
            book_info = f"{book[0]},{book[1]},{book[2]},{book[3]}\n"
            self.file.write(book_info)
        # Kullanıcıya kitabın başarıyla kaldırıldığını bildir
        print(f"Book '{removed_book[0]}' by {removed_book[1]} has been removed from the library.")

        

def main():
    # Programın ana işlevi burada gerçekleşir. Kullanıcıya bir menü gösterilir ve seçim yapması istenir
    # Kullanıcı çıkış yapana kadar menü seçeneklerini göstermeye ve ilgili işlemi gerçekleştirmeye devam eder.
    lib = Library() # Library sınıfından bir nesne oluştur

    while True:
        print("*** MENU ***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("q) Quit")

    
        choice = input("Enter your choice: ")
    # Kullanıcının seçimine göre ilgili fonksiyon çalışır
        if choice == '1':
            lib.list_books()
        elif choice == '2':
            lib.add_book()
        elif choice == '3':
            lib.remove_book()
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please enter a valid option.")  #Kullanıcı yanlış seçim yaparsa bildir.

# Programın ana işlevi burada gerçekleşir. main() fonksiyonu çağrılır, terminalden kod yazmaya gerek kalmadan "run" dendiği an program başlar.
if __name__ == "__main__":
    main()