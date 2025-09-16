import React from "react";

export default function CandidateCard({ candidate }) {
  return (
    <div className="card">
      <div style={{display:"flex", justifyContent:"space-between"}}>
        <div>
          <strong>{candidate.name}</strong> <br />
          <small>{candidate.City}, {candidate.Country}</small>
        </div>
        <div style={{textAlign:"right"}}>
          <div>Score: <strong>{candidate.score}</strong></div>
          <div style={{fontSize:12, color:"#666"}}>{candidate["Monthly Rate"] ? `$${candidate["Monthly Rate"]}/mo` : candidate["Hourly Rate"] ? `$${candidate["Hourly Rate"]}/hr` : ""}</div>
        </div>
      </div>

      <div style={{marginTop:8}}>
        <div style={{fontSize:13}}><strong>Skills:</strong> {candidate.Skills}</div>
        <div style={{marginTop:6, fontSize:12, color:"#444"}}><em>{candidate.reason}</em></div>
      </div>
    </div>
  );
}
