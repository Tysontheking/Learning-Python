class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}"

    def __len__(self):
        return len(self.title)
    

book1 = Book("Python Programming", "John Doe")
print(str(book1))
print("Length of title:", len(book1))  # Output: Length of title: 18