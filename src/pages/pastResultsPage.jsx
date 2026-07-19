import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import DriverStandings from "../components/driverStandings";
import TeamStandings from "../components/teamStandings";
import Schedule from '../components/schedule';
import PastSeasonSelector from '../components/pastSeasonSelector';

import useGetSchedule from '../hooks/getScheduleHook';
import useDriverStandings from '../hooks/driverStandingsHook';
import useTeamStandings from '../hooks/teamStandingsHook';
import useGetSeasonInfo from '../hooks/getSeasonSummaryHook';
import SeasonInfo from '../components/seasonResultsSummary';

function PastResultsPage() {
    const currentYear = new Date().getFullYear();
    const { year } = useParams();

    const schedule = useGetSchedule(year);
    const driverStandings = useDriverStandings(year);
    const teamStandings = useTeamStandings(year);
    const seasonInfo = useGetSeasonInfo(year);
    

    return(
        <>
            <div className = 'past-results-page'>
                <PastSeasonSelector className='lg:col-start-2 lg:row-start-1 scrollbar' year = {currentYear}/>
                <SeasonInfo className='lg:col-start-3 lg:row-start-1 scrollbar' seasonInfo={seasonInfo.data}/>
                <Schedule className='lg:col-start-4 lg:row-start-1 scrollbar' year={year} schedule={schedule.data} loading={schedule.loading}/>
                <DriverStandings className='lg:col-start-2 lg:row-start-2 scrollbar' driverStandings={driverStandings.data} loading={driverStandings.loading}/>
                <TeamStandings className='lg:col-start-3 lg:row-start-2 scrollbar' teamStandings={teamStandings.data} loading={teamStandings.loading}/>
            </div>
        </>
    );
}

export default PastResultsPage;
