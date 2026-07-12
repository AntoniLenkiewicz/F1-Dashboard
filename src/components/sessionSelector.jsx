import { useState, useEffect } from 'react'

function SessionSelector({ className, allSessions, selectedSession, selectSession, loading }) {
    if (loading) {
        return (
        <div className = {`session-selector session-selector-skeleton ${className}`}>
        </div>
        );
    };
    return (
    <div className = {`session-selector ${className}`}>
        <p>Session:{selectedSession}</p>
        {allSessions.map((session)=>(
            <button key = {session} title = {session}
            onClick={()=>selectSession(session)}>{session}</button>
        ))}
    </div>
    );
}


export default SessionSelector;