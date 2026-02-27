import { useState, useEffect } from "react";
import api from "../services/api";

function BookForm({ editingBook, onSuccess }) {
  const [formData, setFormData] = useState({
    title: "",
    isbn: "",
    publication_year: "",
    author_id: "",
    category_id: ""
  });

  useEffect(() => {
    if (editingBook) {
      setFormData(editingBook);
    }
  }, [editingBook]);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = () => {
    if (!formData.title || !formData.isbn) {
      alert("Title and ISBN required");
      return;
    }

    if (editingBook) {
      api.put(`/books/${editingBook.id}`, formData)
        .then(() => onSuccess());
    } else {
      api.post("/books", formData)
        .then(() => onSuccess());
    }

    setFormData({
      title: "",
      isbn: "",
      publication_year: "",
      author_id: "",
      category_id: ""
    });
  };

  return (
    <div style={{ marginBottom: "20px" }}>
      <h3>{editingBook ? "Edit Book" : "Add Book"}</h3>

      <input name="title" placeholder="Title" value={formData.title} onChange={handleChange} />
      <input name="isbn" placeholder="ISBN" value={formData.isbn} onChange={handleChange} />
      <input name="publication_year" placeholder="Year" value={formData.publication_year} onChange={handleChange} />
      <input name="author_id" placeholder="Author ID" value={formData.author_id} onChange={handleChange} />
      <input name="category_id" placeholder="Category ID" value={formData.category_id} onChange={handleChange} />

      <button onClick={handleSubmit}>
        {editingBook ? "Update" : "Create"}
      </button>
    </div>
  );
}

export default BookForm;