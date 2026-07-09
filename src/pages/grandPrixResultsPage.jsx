import { useState, useEffect } from 'react';

import EventInformation from '../components/eventInformation';
import ResultsTable from '../components/resultsTable';

import useGetEventInfo from '../hooks/eventInfoHook';
import useGetResults from '../hooks/getResultsHook';

function GrandPrixResultsPage() {
    const year = 2026;
    const gp = "British";
    
    const eventInfo = useGetEventInfo({year, gp});
    const results = useGetResults({year, gp});

    return (
        <>
            <div className='gp-results-page'>
                <EventInformation className = 'lg:col-start-2 lg:row-start-1' eventInfo={eventInfo.data} loading={eventInfo.loading} />
                <ResultsTable className = 'lg:col-start-2 lg:row-start-2' results={results.data.sessionResults} columns={results.data.columns} loading={results.loading} />
            </div>
        </>
    );
};

export default GrandPrixResultsPage;

