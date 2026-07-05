import { useState, useEffect } from 'react'
import { Routes, Route, Link } from 'react-router-dom';
import './index.css'
import HomePage from './pages/homePage'
import './App.css'
import Navbar from './components/navbar';

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
      <Navbar />

      <Routes>
        <Route path='/' element={<HomePage />} />
        <Route path='/time' element={<Time />} />
      </Routes>
      </section>
    </>
  );
}

export default App