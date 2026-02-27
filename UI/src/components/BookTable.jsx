import api from "../services/api";

function BookTable({ books, onEdit, onDelete }) {

  const handleDelete = (id) => {
    if (window.confirm("Are you sure you want to delete?")) {
      api.delete(`/books/${id}`)
        .then(() => onDelete())
        .catch(() => alert("Book not found"));
    }
  };

  return (
    <table border="1" cellPadding="8">
      <thead>
        <tr>
          <th>Title</th>
          <th>ISBN</th>
          <th>Year</th>
          <th>Author</th>
          <th>Category</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {books.map(book => (
          <tr key={book.id}>
            <td>{book.title}</td>
            <td>{book.isbn}</td>
            <td>{book.publication_year}</td>
            <td>{book.author_id}</td>
            <td>{book.category_id}</td>
            <td>
              <button onClick={() => onEdit(book)}>Edit</button>
              <button onClick={() => handleDelete(book.id)}>Delete</button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default BookTable;