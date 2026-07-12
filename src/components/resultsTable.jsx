import { useState, useEffect } from 'react';

function ResultsTable({ className='', results, columns,  loading}) {
    if (loading){
        return (
            <div className = {`results-table results-table-skeleton ${className}`}>
            <table>
                <thead>
                    <tr>
                        <th>Loading</th>
                    </tr>
                </thead>
            </table>
        </div>
        )
    }
    return (
        <div className = {`results-table ${className}`}>
            <table>
                <thead>
                    <tr>
                        {columns.map((column) => (
                        <th key={column}>{column}</th>
                        ))}
                    </tr>
                </thead>
                <tbody>
                    {results
                    .sort((a, b) => a.Pos - b.Pos)
                    .map((driver, index) =>
                    <tr key={index}>
                        {columns
                        .map((column)=>
                        <td key= {column}>{driver[column]}</td>
                        )}
                    </tr>
                    )}
                </tbody>
            </table>
        </div>
    );
};

export default ResultsTable;