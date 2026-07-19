import {useState, useEffect} from 'react'


function SeasonInfo({className, seasonInfo, loading}){
    if (loading) {
        return(
        <div className = {`season-info season-info-skeleton ${className}`}>
            <h1>Season:</h1>
        </div>
        );
    }
    return(
        <div className = {`season-info ${className}`}>
            <h1>Season: {seasonInfo.year}</h1>
            <h1>Rounds: {seasonInfo.rounds}</h1>
        </div>
    );
};

export default SeasonInfo;