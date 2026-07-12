import { useState, useEffect, useRef } from 'react';

import EventInformation from '../components/eventInformation';
import ResultsTable from '../components/resultsTable';
import SessionSelector from '../components/sessionSelector';

import useGetEventInfo from '../hooks/eventInfoHook';
import useGetResults from '../hooks/getResultsHook';

function GrandPrixResultsPage() {
    const year = 2026;
    const gp = "British";
    const [selectedSession, setSelectedSession] = useState();
    const sessionsMap = useRef(new Map());

    const eventInfo = useGetEventInfo({year, gp});
    const isCached = sessionsMap.current.get(selectedSession);
    const results = useGetResults({year, gp, session: selectedSession});
    const sessions = results.data?.allSessionNames ?? [];

    useEffect(()=> {
        if (!selectedSession && results.data?.sessionName){
        setSelectedSession(results.data.sessionName);
        };
    }, [results.data.sessionName]);

    useEffect(() => {
        if (selectedSession && results.data && selectedSession == results.data.sessionName) {
            sessionsMap.current.set(selectedSession, results.data);
        }
    }, [selectedSession, results.data]);

    function handleSelectSession(data){
        setSelectedSession(data);
    };
    const currentSession = sessionsMap.current.get(selectedSession);
    const sessionData = currentSession ?? results.data;
    const loading = !currentSession && results.loading;

    return (
        <>
            <div className='gp-results-page'>
                <EventInformation className = 'lg:col-start-2 lg:row-start-1' eventInfo={eventInfo.data} loading={eventInfo.loading} />
                <ResultsTable className = 'lg:col-start-2 lg:row-start-2' results={sessionData.sessionResults} columns={sessionData.columns} loading={loading} />
                <SessionSelector className = 'lg:col-start-4 lg:row-start-1' selectedSession={selectedSession} selectSession={handleSelectSession} allSessions={sessions} loading = {!(sessions)} />
            </div>
        </>
    );
};

export default GrandPrixResultsPage;

