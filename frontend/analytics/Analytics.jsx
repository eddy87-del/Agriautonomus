"""Analytics Component"""

const Analytics = () => {
  return (
    <div className="analytics">
      <h2>Farm Analytics</h2>
      <div className="chart-container">
        <div id="health-chart">Health Chart</div>
        <div id="productivity-chart">Productivity Chart</div>
      </div>
    </div>
  );
};

export default Analytics;
