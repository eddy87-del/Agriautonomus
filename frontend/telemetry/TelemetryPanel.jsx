"""Telemetry Display Component"""

const TelemetryPanel = () => {
  return (
    <div className="telemetry-panel">
      <h2>Live Telemetry</h2>
      <div className="telemetry-data">
        <div className="metric">
          <span>Battery</span>
          <span id="battery">--</span>
        </div>
        <div className="metric">
          <span>GPS</span>
          <span id="gps">--</span>
        </div>
        <div className="metric">
          <span>Altitude</span>
          <span id="altitude">--</span>
        </div>
      </div>
    </div>
  );
};

export default TelemetryPanel;
