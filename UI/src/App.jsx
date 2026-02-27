import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Books from "./pages/Books";
import Authors from "./pages/Authors";
import AuthorDetails from "./pages/AuthorDetails";
import Stats from "./pages/Stats";
import './App.css';
function App() {
  return (
    <BrowserRouter>
      <header className="header">
        <h1>Library Management System</h1>
      </header>

      <div className="page-content">
        <nav>
          <Link to="/">Dashboard</Link>
          <Link to="/books">Books</Link>
          <Link to="/authors">Authors</Link>
          <Link to="/stats">Stats</Link>
        </nav>

        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/books" element={<Books />} />
          <Route path="/authors" element={<Authors />} />
          <Route path="/authors/:id" element={<AuthorDetails />} />
          <Route path="/stats" element={<Stats />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}
export default App;