```python
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
```
Output:
```
<Book: 1984>
```
```python
retrieved_book = Book.objects.get(title="1984")
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)
```
Output:
```
1984 George Orwell 1949
```
```python
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
updated_book = Book.objects.get(id=retrieved_book.id)
print(updated_book.title)
```
Output:
```
Nineteen Eighty-Four
```
```python
retrieved_book.delete()
books = Book.objects.all()
print(books)
```
Output:
```
<QuerySet []>
```
