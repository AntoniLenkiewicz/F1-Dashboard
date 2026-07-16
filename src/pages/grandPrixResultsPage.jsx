import { useState, useEffect, useRef } from 'react';
import { useParams } from 'react-router-dom';
import EventInformation from '../components/eventInformation';
import ResultsTable from '../components/resultsTable';
import SessionSelector from '../components/sessionSelector';

import useGetEventInfo from '../hooks/eventInfoHook';

function GrandPrixResultsPage() {
    const { year, gp } = useParams()
    const [selectedSession, setSelectedSession] = useState();
    const [sessionData, setSessionData] = useState({
        sessionName: '',
        results: [],
        columns: [],
        allSessions: []
    });
    const [loading, setLoading] = useState(false);
    const sessionsMap = useRef(new Map());
    const eventInfo = useGetEventInfo({year, gp});

    async function loadSession(year, gp, session=''){
        if (!sessionsMap.current.get(session)) {
            setLoading(true);
            const response = await fetch(`/api/getgpresults?year=${year}&gp=${gp}&session=${session}`, {cache: 'no-store'});
            const data = await response.json();
            const sessionName = data.sessionName;

            setSelectedSession(sessionName);
            sessionsMap.current.set(sessionName, data);
            setSessionData(data);
            setLoading(false);

        } else {
            const data = sessionsMap.current.get(session);
            setSessionData(data);
        };
    };
    useEffect(() =>{
        if (!selectedSession && !loading) {
            loadSession(year, gp);
        }
    }, [eventInfo.data]);

    function handleSelectSession(data){
        setSelectedSession(data);
        loadSession(year, gp, data);
    };

    return (
        <>
            <div className='gp-results-page'>
                <EventInformation className = 'row-start-1 lg:col-start-2 lg:row-start-1' eventInfo={eventInfo.data} loading={eventInfo.loading} />
                <ResultsTable className = 'row-start-3 lg:col-start-2 lg:row-start-2' results={sessionData.results} columns = {sessionData.columns} loading={loading} />
                <SessionSelector className = 'row-start-2 lg:col-start-4 lg:row-start-1' selectedSession={selectedSession} selectSession={handleSelectSession} allSessions={sessionData.allSessions} loading = {!sessionData.allSessions} />
            </div>
        </>
    );
};

export default GrandPrixResultsPage;

