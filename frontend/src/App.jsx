import { useState, useEffect } from 'react';

function App() {
  const [status, setStatus] = useState(null);
  const [threats, setThreats] = useState([]);
  const [missionData, setMissionData] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchStatus();
    const interval = setInterval(fetchThreats, 5000);
    return () => clearInterval(interval);
  }, []);

  const fetchStatus = async () => {
    try {
      const res = await fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:8000'}/api/status`);
      const data = await res.json();
      setStatus(data);
    } catch (err) {
      console.error(err);
      setStatus({ status: 'offline' });
    }
  };

  const fetchThreats = async () => {
    try {
      const res = await fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:8000'}/api/threats`);
      const data = await res.json();
      if (data.status === 'success') {
        setThreats(data.data);
      }
    } catch (err) {
      console.error(err);
    }
  };

  const runMission = async () => {
    setLoading(true);
    try {
      const res = await fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:8000'}/api/mission`);
      const data = await res.json();
      if (data.status === 'success') {
        setMissionData(data.data);
      }
    } catch (err) {
      console.error(err);
    }
    setLoading(false);
  };

  const getThreatClass = (type) => {
    if (type.includes('Stealth')) return 'stealth';
    if (type.includes('UAV')) return 'uav';
    return '';
  };

  return (
    <div className="app-container">
      <header>
        <div className="logo">ASSRS</div>
        <div className={`status-badge ${status?.status === 'offline' ? 'offline' : ''}`}>
          {status?.status === 'offline' ? 'SYSTEM OFFLINE' : 'SYSTEM ONLINE'}
        </div>
      </header>

      <div className="dashboard-grid">
        <div className="glass-panel">
          <h2>Mission Control</h2>
          <div style={{ marginBottom: '2rem' }}>
            <div className="stat-value">{missionData ? missionData.length : 0}</div>
            <div style={{ color: 'var(--text-muted)' }}>Sensors Responding</div>
          </div>
          <button className="btn" onClick={runMission} disabled={loading}>
            {loading ? 'Initializing...' : 'Execute Audit Mission'}
          </button>
        </div>

        <div className="glass-panel" style={{ gridColumn: 'span 2' }}>
          <h2>Active Threats ({threats.length})</h2>
          {threats.length === 0 ? (
            <div style={{ color: 'var(--text-muted)', fontStyle: 'italic', padding: '1rem' }}>
              No active threats detected. Awaiting telemetry...
            </div>
          ) : (
            <ul className="threat-list">
              {threats.map((t, idx) => (
                <li key={idx} className={`threat-item ${getThreatClass(t.type)}`} style={{ animationDelay: `${idx * 0.1}s` }}>
                  <div>
                    <div className="threat-id">{t.id}</div>
                    <div className="threat-type">{t.type}</div>
                  </div>
                  <div className="threat-dist">{t.distance}m</div>
                </li>
              ))}
            </ul>
          )}
        </div>

        <div className="glass-panel">
          <h2>System Logs</h2>
          <div style={{ color: 'var(--text-muted)', fontSize: '0.9rem', lineHeight: '1.6' }}>
            {status ? (
              <>
                <div>[SYS] Encryption: {status.encryption}</div>
                <div>[SYS] Nodes Active: {status.active_sensors}</div>
                <div>[SYS] Backend connection established.</div>
              </>
            ) : (
              <div>[ERR] Failed to connect to core server.</div>
            )}
            {missionData && <div style={{ color: 'var(--success)', marginTop: '1rem' }}>[MSG] Mission completed successfully. Stream processed.</div>}
            <div className="sensors-grid" style={{ marginTop: '1rem' }}>
              {Array.from({ length: 50 }).map((_, i) => (
                <div key={i} className={`sensor-dot ${missionData && i < missionData.length ? 'active' : ''}`} style={{ transitionDelay: `${Math.random() * 0.5}s` }}></div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
