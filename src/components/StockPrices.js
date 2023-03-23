import { useState, useEffect } from 'react';
import LineChart from './LineChart';

function StockPrices() {
  const [stockPrices, setStockPrices] = useState(null);

  useEffect(() => {
    const interval = setInterval(() => {
      fetch('http://localhost:8000/api/get_stocks/')
        .then(response => response.json())
        .then(data => setStockPrices(data));
    }, 20000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h2>Stock Prices</h2>
      {stockPrices && <LineChart data={stockPrices} />}
    </div>
  );
}

export default StockPrices;