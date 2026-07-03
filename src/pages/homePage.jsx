import { useState, useEffect } from 'react';
import DriverStandings from "../components/driverStandings";
import TeamStandings from "../components/teamStandings";
import NextEvent from '../components/nextEvent';
function HomePage() {
    const currentYear = new Date().getFullYear();
    const [year, setYear] = useState(currentYear);
    const [driverStandings, setDriverStandings] = useState([]);
    const [teamStandings, setTeamStandings] = useState([]);
    const [nextEvent, setNextEvent] = useState([]);

    useEffect(() => {
        fetch(`/api/driverstandings?year=${year}`)
        .then(res => res.json())
        .then(data => setDriverStandings(data))
    }, [year]);
   
    useEffect(() => {
        fetch(`/api/teamstandings?year=${year}`)
        .then(res => res.json())
        .then(data => setTeamStandings(data))
    }, [year]);

    useEffect(() => {
        fetch('/api/getnextevent')
        .then(res => res.json())
        .then(data => setNextEvent(data))
    }, []);

  return (
    <>
        <div className = 'grid grid-cols-6 grid-rows-12 gap-5'>
            <NextEvent className = 'col-start-2 row-start-1' nextEvent={nextEvent} />
            <DriverStandings className = 'col-start-2 row-start-2' driverStandings={driverStandings} />
            <TeamStandings className = 'col-start-3 row-start-2' teamStandings = {teamStandings} />
        </div>
    </>
  );
}

export default HomePage;