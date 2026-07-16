import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

import useGetSchedule from '../hooks/getScheduleHook';
import Schedule from '../components/schedule';

function PastResultsPage() {
    const { year } = useParams();
    const schedule = useGetSchedule(year);

    return(
        <>
            <div className = 'past-results-page'>
                <Schedule className='lg:col-start-4 lg:row-start-1 scrollbar' year={year} schedule={schedule.data} loading={schedule.loading}/>
            </div>
        </>
    );
}

export default PastResultsPage;