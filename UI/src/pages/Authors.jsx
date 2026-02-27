import { useEffect, useState } from "react";
import api from "../services/api";
import { Link } from "react-router-dom";

function Authors() {
  const [authors, setAuthors] = useState([]);
  const [name, setName] = useState("");
  const [editingAuthor, setEditingAuthor] = useState(null);

  const fetchAuthors = () => {
    api.get("/authors")
      .then(res => setAuthors(res.data));
  };

  useEffect(() => {
    fetchAuthors();
  }, []);

  const saveAuthor = () => {
    if (!name.trim()) return;

    if (editingAuthor) {
      api.put(`/authors/${editingAuthor.id}`, { name })
        .then(() => {
          setEditingAuthor(null);
          setName("");
          fetchAuthors();
        });
    } else {
      api.post("/authors", { name })
        .then(() => {
          setName("");
          fetchAuthors();
        });
    }
  };

  const deleteAuthor = (id) => {
    if (window.confirm("Delete author?")) {
      api.delete(`/authors/${id}`)
        .then(fetchAuthors)
        .catch(err =>
          alert(err.response?.data?.detail || "Error deleting author")
        );
    }
  };

  const handleEdit = (author) => {
    setEditingAuthor(author);
    setName(author.name);
  };

  return (
    <div>
      <h1>Authors</h1>

      <input
        placeholder="Author Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <button onClick={saveAuthor}>
        {editingAuthor ? "Update" : "Add"}
      </button>

      {editingAuthor && (
        <button
          onClick={() => {
            setEditingAuthor(null);
            setName("");
          }}
          style={{ marginLeft: "10px" }}
        >
          Cancel
        </button>
      )}

      <ul style={{ marginTop: "20px" }}>
        {authors.map(author => (
         <li key={author.id}>
  {author.name}

  <div className="author-actions">
    <button onClick={() => handleEdit(author)}>Edit</button>

    <Link
      to={`/authors/${author.id}`}
      className="view-btn"
    >
      View
    </Link>

    <button onClick={() => deleteAuthor(author.id)}>
      Delete
    </button>
  </div>
</li>
        ))}
      </ul>
    </div>
  );
}

export default Authors;