import { useState, useEffect } from 'react';
import DriverStandings from "../components/driverStandings";
import TeamStandings from "../components/teamStandings";

function HomePage() {
    const currentYear = new Date().getFullYear()
    const [year, setYear] = useState(currentYear)
    const [driverStandings, setDriverStandings] = useState([])
    const [teamStandings, setTeamStandings] = useState([])
    useEffect(() => {
        fetch(`/api/driverstandings?year=${year}`)
        .then(res => res.json())
        .then(data => setDriverStandings(data))
    }, [year])
   

    useEffect(() => {
        fetch(`/api/teamstandings?year=${year}`)
        .then(res => res.json())
        .then(data => setTeamStandings(data))
    }, [year]) 

  return (
    <>
        <div className = 'grid grid-cols-4 grid-rows-4 gap-5' >
            <DriverStandings className = 'col-start-1 row-start-4' driverStandings={driverStandings} />
            <TeamStandings className = 'col-start-2 row-start-4' teamStandings = {teamStandings} />
        </div>
    </>
  );
}

export default HomePage;