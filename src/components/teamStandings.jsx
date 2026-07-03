import { useState, useEffect } from 'react'


function TeamStandings({ className = '', teamStandings }){
    return (
    <div className={`standings-table ${className}`}>
        <table>
            <thead>
            <tr>
                <th>Pos</th>
                <th>Team</th>
                <th>Points</th>
            </tr>
            </thead>
            <tbody>
            {Object.entries(teamStandings)
            .sort((a, b) => b[1] - a[1])
            .map(([teamName, points], index) => (
                <tr key={teamName}>
                <td>{index + 1}</td>
                <td>{teamName}</td>
                <td>{points}</td>
                </tr>
            ))}
            </tbody>
        </table>
        </div>
    );
}

export default TeamStandings;