import { useState, useEffect } from 'react'
import { Routes, Route, Link } from 'react-router-dom';
import './App.css'

function Time() {
  const [currentTime, setCurrentTime] = useState(0);
  useEffect(() => {
    fetch('/api/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);
  return <p>The current time is {new Date(currentTime * 1000).toLocaleString()}.</p>;
}

function HomePage() {
  const currentYear = new Date().getFullYear()
  const [year, setYear] = useState(currentYear)
  const [standings, setStandings] = useState([])

  useEffect(() => {
    fetch(`/api/standings?year=${year}`)
      .then(res => res.json())
      .then(data => setStandings(data))
  }, [year])
  const sorted = Object.entries(standings)
    .sort((a, b) => b[1] - a[1])


  return (
  <div>
      <table>
        <thead>
          <tr>
            <th>Pos</th>
            <th>Driver</th>
            <th>Points</th>
          </tr>
        </thead>
        <tbody>
          {sorted.map(([driver, points], index) => (
            <tr key={driver}>
              <td>{index + 1}</td>
              <td>{driver}</td>
              <td>{points}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function App() {
  return (
    <>
      <section id="center">
        <HomePage />
      <nav>
        <Link to="/time">Time</Link>
      </nav>

      <Routes>
        <Route path="/time" element={<Time />} />
      </Routes>
      </section>
    </>
  )
}

export default App