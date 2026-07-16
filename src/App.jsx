import { useState, useEffect } from 'react'
import { Routes, Route, Link } from 'react-router-dom';
import './index.css'
import './App.css'
import Navbar from './components/navbar';
import HomePage from './pages/homePage'
import GrandPrixResultsPage from './pages/grandPrixResultsPage';
import PastResultsPage from './pages/pastResultsPage';

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
      <Navbar />
      <section id="center">
        <Routes>
          <Route path='/' element={<HomePage />} />
          <Route path='/time' element={<Time />} />
          <Route path='/pastresults/:year/:gp' element={<GrandPrixResultsPage />} />
          <Route path='/pastresults/:year' element = {<PastResultsPage />} />
        </Routes>
      </section>
    </>
  );
}

export default App