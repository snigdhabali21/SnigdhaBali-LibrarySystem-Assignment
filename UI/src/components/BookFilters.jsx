import { useState } from "react";

function BookFilters({ setFilters }) {
  const [localFilters, setLocalFilters] = useState({});

  const handleChange = (e) => {
    setLocalFilters({
      ...localFilters,
      [e.target.name]: e.target.value
    });
  };

  const applyFilters = () => {
    setFilters(localFilters);
  };

  return (
    <div style={{ marginBottom: "20px" }}>
      <input
        name="author_id"
        placeholder="Author ID"
        onChange={handleChange}
      />

      <input
        name="category_id"
        placeholder="Category ID"
        onChange={handleChange}
      />

      <input
        name="year"
        placeholder="Exact Year"
        onChange={handleChange}
      />

      <input
        name="min_year"
        placeholder="Min Year"
        onChange={handleChange}
      />

      <input
        name="max_year"
        placeholder="Max Year"
        onChange={handleChange}
      />

      <input
        name="limit"
        placeholder="Limit"
        onChange={handleChange}
      />

      <button onClick={applyFilters}>Apply</button>
    </div>
  );
}

export default BookFilters;