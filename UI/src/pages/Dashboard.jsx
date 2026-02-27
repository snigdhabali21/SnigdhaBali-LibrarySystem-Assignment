import { useEffect, useState } from "react";
import api from "../services/api";

function Dashboard() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    api.get("/books/insights")
      .then((res) => {
        setData(res.data);
      })
      .catch(() => {
        setError(true);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading dashboard...</p>;
  if (error) return <p>Failed to load insights.</p>;
  if (!data) return <p>No data available.</p>;

    const totalBooks = data.valid_books.length;

  const averageYear =
    totalBooks > 0
      ? Math.round(
          data.valid_books.reduce((sum, book) => sum + book.publication_year, 0) /
            totalBooks
        )
      : "N/A";

 return (
    <div style={{ padding: "20px" }}>
      <h2>Library Dashboard</h2>

      <h3>Total Books: {totalBooks}</h3>
      <h3>Average Publication Year: {averageYear}</h3>

      <h2>Books per author</h2>
      <ul>
        {data.top_authors.map((author, index) => (
          <li key={index}>
            {author.author} — {author.book_count}
          </li>
        ))}
      </ul>
      <h2>Books per Category</h2>
      {data.books_per_category && data.books_per_category.length === 0 ? (
            <p>No category data</p>
      ) : (
      <ul>
    {data.books_per_category?.map((item, index) => (
      <li key={index}>
        {item.category} — {item.count}
      </li>
    ))}
  </ul>
)}

      <h2>Busy Years</h2>
      {Object.keys(data.busy_years).length === 0 ? (
        <p>No busy years</p>
      ) : (
        Object.entries(data.busy_years).map(([year, books]) => (
          <div key={year}>
            <strong>{year}</strong>
            <ul>
              {books.map((title, idx) => (
                <li key={idx}>{title}</li>
              ))}
            </ul>
          </div>
        ))
      )}
    </div>
  );
}

export default Dashboard;