import { useState, useEffect } from 'react'
import { Routes, Route, Link } from 'react-router-dom';
import './index.css'
import HomePage from './pages/homePage'
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


function App() {
  return (
    <>
      <section id="center">
      <nav>
        <Link to='/'>Home</Link>
        <Link to='/time'>Time</Link>
      </nav>

      <Routes>
        <Route path='/' element={<HomePage />} />
        <Route path='/time' element={<Time />} />
      </Routes>
      </section>
    </>
  )
}

export default App