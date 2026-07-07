import { useState, useEffect } from 'react';
import DriverStandings from "../components/driverStandings";
import TeamStandings from "../components/teamStandings";
import NextEvent from '../components/nextEvent';
import Schedule from '../components/schedule';
import useDriverStandings from '../hooks/driverStandingsHook';
import useTeamStandings from '../hooks/teamStandingsHook';
import useGetNextEvent from '../hooks/getNextEventHook';
import useGetSchedule from '../hooks/getScheduleHook';

function HomePage() {
    const currentYear = new Date().getFullYear();
    const [year, setYear] = useState(currentYear);

    const driverStandings = useDriverStandings(year);
    const teamStandings = useTeamStandings(year);
    const nextEvent = useGetNextEvent();
    const schedule = useGetSchedule();

  return (
    <>
        <div className='home-page'>
            <NextEvent className='lg:col-start-2 lg:row-start-1' nextEvent={nextEvent.data} loading={nextEvent.loading} />
            <DriverStandings className='lg:col-start-2 lg:row-start-2 scrollbar' driverStandings={driverStandings.data} loading={driverStandings.loading}/>
            <TeamStandings className='lg:col-start-3 lg:row-start-2 scrollbar' teamStandings={teamStandings.data} loading={teamStandings.loading}/>
            <Schedule className='lg:col-start-4 lg:row-start-1 scrollbar' schedule={schedule.data} loading={schedule.loading}/>
        </div>
    </>
  );
}

export default HomePage;