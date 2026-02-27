import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import api from "../services/api";

function AuthorDetails() {
  const { id } = useParams();
  const [author, setAuthor] = useState(null);
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const authorRes = await api.get(`/authors/${id}`);
        const statsRes = await api.get(`/authors/${id}/stats`);

        console.log("Author response:", authorRes.data);
        console.log("Stats response:", statsRes.data);

        setAuthor(authorRes.data);
        setStats(statsRes.data);
      } catch (error) {
        console.error("Error loading author:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [id]);

  if (loading) return <p>Loading...</p>;

  if (!author) return <p>Author not found</p>;

  return (
    <div>
      <Link to="/authors">← Back</Link>

      <h1>{author.name}</h1>

      {author.books && author.books.length > 0 ? (
        <ul>
          {author.books.map(book => (
            <li key={book.id}>
              {book.title} ({book.publication_year})
            </li>
          ))}
        </ul>
      ) : (
        <p></p>
      )}

      {stats && (
        <div style={{ marginTop: "20px" }}>
          <h3>Earliest Book: {stats.earliest_book || "N/A"}</h3>
          <h3>Latest Book: {stats.latest_book || "N/A"}</h3>
        </div>
      )}
    </div>
  );
}

export default AuthorDetails;