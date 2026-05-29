"""Frontend Dashboard Component"""

const Dashboard = () => {
  return (
    <div className="dashboard">
      <h1>Agriautonomous Control Center</h1>
      <div className="dashboard-grid">
        <div className="widget">Map View</div>
        <div className="widget">Telemetry</div>
        <div className="widget">Missions</div>
        <div className="widget">Alerts</div>
      </div>
    </div>
  );
};

export default Dashboard;
