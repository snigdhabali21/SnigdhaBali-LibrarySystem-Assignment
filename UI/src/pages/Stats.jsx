import { useEffect, useState } from "react";
import api from "../services/api";

function Stats() {
  const [insights, setInsights] = useState(null);
  const [authors, setAuthors] = useState([]);
  const [selectedAuthor, setSelectedAuthor] = useState("");
  const [authorStats, setAuthorStats] = useState(null);
  const [firstNBooks, setFirstNBooks] = useState([]);

  useEffect(() => {
    // Load general insights
    api.get("/books/insights").then(res => setInsights(res.data));

    // Load authors list
    api.get("/authors").then(res => setAuthors(res.data));

    // Load first 5 books sorted by title
    api.get("/books", { params: { sort: "title", limit: 5 } })
      .then(res => setFirstNBooks(res.data));
  }, []);

  const fetchAuthorStats = (id) => {
    setSelectedAuthor(id);

    if (!id) return;

    api.get(`/authors/${id}/stats`)
      .then(res => setAuthorStats(res.data));
  };

  if (!insights) return <p>Loading stats...</p>;

  return (
    <div>
      <h3>Library Stats</h3>


      {/* Average Year */}
      <h3>
        Average Publication Year:{" "}
        {insights.average_year || "N/A"}
      </h3>

      <hr />

      {/* Author Selection */}
      <h2>Select Author</h2>

      <select
        value={selectedAuthor}
        onChange={(e) => fetchAuthorStats(e.target.value)}
      >
        <option value="">-- Select Author --</option>
        {authors.map(author => (
          <option key={author.id} value={author.id}>
            {author.name}
          </option>
        ))}
      </select>

      {authorStats && (
        <div style={{ marginTop: "25px" }}>
          <h4>
            Earliest Book: {authorStats.earliest_book || "N/A"}
          </h4>
          <h4>
            Latest Book: {authorStats.latest_book || "N/A"}
          </h4>
          <h4>
            At least one book?{" "}
            {authorStats.earliest_book ? "Yes" : "No"}
          </h4>
        </div>
      )}

      <hr />

      {/* First N Books Sorted */}
      <h3>First 5 Books (Sorted by Title)</h3>
      <ul>
        {firstNBooks.map(book => (
          <li key={book.id}>{book.title}</li>
        ))}
      </ul>

      <hr />

      {/* Distinct Authors */}
      <h3>Distinct Authors</h3>
      <ul>
        {authors.map(author => (
          <li key={author.id}>{author.name}</li>
        ))}
      </ul>

      <hr />

      {/*  Books per Category */}
      <h3>Books Per Category</h3>
      <ul>
        {insights.books_per_category.map(cat => (
          <li key={cat.category}>
            {cat.category}: {cat.count}
          </li>
        ))}
      </ul>

    </div>
  );
}

export default Stats;