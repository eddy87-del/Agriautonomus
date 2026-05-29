"""Missions Control Component"""

const MissionsPanel = () => {
  return (
    <div className="missions-panel">
      <h2>Active Missions</h2>
      <div className="mission-controls">
        <button>New Mission</button>
        <button>Arm</button>
        <button>Execute</button>
        <button>Abort</button>
      </div>
      <div className="mission-list" id="mission-list"></div>
    </div>
  );
};

export default MissionsPanel;
