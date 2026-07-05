import { useState, useEffect } from 'react';
import DriverStandings from "../components/driverStandings";
import TeamStandings from "../components/teamStandings";
import NextEvent from '../components/nextEvent';
import Schedule from '../components/schedule';

function HomePage() {
    const currentYear = new Date().getFullYear();
    const [year, setYear] = useState(currentYear);
    const [driverStandings, setDriverStandings] = useState([]);
    const [teamStandings, setTeamStandings] = useState([]);
    const [nextEvent, setNextEvent] = useState([]);
    const [schedule, setSchedule] = useState([]);

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

    useEffect(() => {
        fetch('/api/getschedule')
        .then(res => res.json())
        .then(data => setSchedule(data))
    }, []);

  return (
    <>
        <div className = 'grid grid-cols-5 grid-rows-4 gap-5'>
            <NextEvent className = 'col-start-2 row-start-1' nextEvent={nextEvent} />
            <DriverStandings className = 'col-start-2 row-start-2 scrollbar' driverStandings={driverStandings} />
            <TeamStandings className = 'col-start-3 row-start-2 scrollbar' teamStandings = {teamStandings} />
            <Schedule className = 'col-start-4 row-start-1 scrollbar' schedule={schedule} />
        </div>
    </>
  );
}

export default HomePage;