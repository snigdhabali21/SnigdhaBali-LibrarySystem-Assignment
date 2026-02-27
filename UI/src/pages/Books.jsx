// import { useEffect, useState } from "react";
// import api from "../services/api";
// import BookTable from "../components/BookTable";
// import BookForm from "../components/BookForm";
// import BookFilters from "../components/BookFilters";

// function Books() {
//   const [books, setBooks] = useState([]);
//   const [filters, setFilters] = useState({});
//   const [loading, setLoading] = useState(true);
//   const [editingBook, setEditingBook] = useState(null);

//   const fetchBooks = () => {
//     setLoading(true);
//     api.get("/books", { params: filters })
//       .then(res => setBooks(res.data))
//       .finally(() => setLoading(false));
//   };

//   useEffect(() => {
//     fetchBooks();
//   }, [filters]);

//   return (
//     <div>
//       <h1>Books Management</h1>

//       <BookFilters setFilters={setFilters} />

//       <BookForm
//         editingBook={editingBook}
//         onSuccess={() => {
//           setEditingBook(null);
//           fetchBooks();
//         }}
//       />

//       {loading ? (
//         <p>Loading...</p>
//       ) : books.length === 0 ? (
//         <p>No books found</p>
//       ) : (
//         <BookTable
//           books={books}
//           onEdit={setEditingBook}
//           onDelete={fetchBooks}
//         />
//       )}
//     </div>
//   );
// }

// export default Books;
import { useEffect, useState } from "react";
import api from "../services/api";
import BookTable from "../components/BookTable";
import BookForm from "../components/BookForm";
import BookFilters from "../components/BookFilters";

function Books() {
  const [books, setBooks] = useState([]);
  const [filters, setFilters] = useState({});
  const [loading, setLoading] = useState(true);
  const [editingBook, setEditingBook] = useState(null);
  const [showForm, setShowForm] = useState(false);

  const fetchBooks = () => {
    setLoading(true);
    api.get("/books", { params: filters })
      .then(res => setBooks(res.data))
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    fetchBooks();
  }, [filters]);

  return (
    <div>
      <h1>Books Management</h1>

      <BookFilters setFilters={setFilters} />

      {/* Add Book Button */}
      <button
        onClick={() => {
          setEditingBook(null);
          setShowForm(true);
        }}
        style={{ marginBottom: "15px" }}
      >
        + Add Book
      </button>

      {/* Show Form Conditionally */}
      {showForm && (
        <BookForm
          editingBook={editingBook}
          onSuccess={() => {
            setShowForm(false);
            fetchBooks();
          }}
          onCancel={() => setShowForm(false)}
        />
      )}

      {loading ? (
        <p>Loading...</p>
      ) : books.length === 0 ? (
        <p>No books found</p>
      ) : (
        <BookTable
          books={books}
          onEdit={(book) => {
            setEditingBook(book);
            setShowForm(true);
          }}
          onDelete={fetchBooks}
        />
      )}
    </div>
  );
}

export default Books;