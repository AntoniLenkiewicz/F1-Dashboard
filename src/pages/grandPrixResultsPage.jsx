import { useState, useEffect } from 'react';

import EventInformation from '../components/eventInformation';

import useGetEventInfo from '../hooks/eventInfoHook';

function GrandPrixResultsPage() {
    const year = 2026;
    const gp = "British Grand Prix";
    
    const eventInfo = useGetEventInfo({year, gp})

    return (
        <>
            <div className='gp-results-page'>
                <EventInformation className = 'lg:col-start-2 lg:row-start-1' eventInfo={eventInfo.data} loading={eventInfo.loading} />
            </div>
        </>
    );
};

export default GrandPrixResultsPage;

