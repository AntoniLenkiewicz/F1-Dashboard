import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

function PastSeasonSelector({className, year, loading}){
    const season = []
    for (year; year> 1949; year--) {
        season.push(year);
    };
    return(
        <div className = {`past-season ${className}`}>
            <h1>Select Season</h1>
            <nav>
                {season.map((season)=>(
                    <>
                <Link to = {`/pastresults/${season}`}>
                    <hr/>
                    <p>{season} season</p>
                </Link>
                </>
            ))}
            </nav>
        </div>
    );
};

export default PastSeasonSelector;