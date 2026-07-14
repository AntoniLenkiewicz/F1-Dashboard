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
        {allSessions.map((session)=>(
            <button className={(selectedSession==session) ? 'session-selected' : 'session-not-selected'} key = {session} title = {session}
            onClick={()=>selectSession(session)}>{session}</button>
        ))}
    </div>
    );
}


export default SessionSelector;