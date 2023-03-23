import { useState, useEffect } from "react";
import LineCharts from "./LineCharts";

function ChartContainer() {
  const [prices, setPrices] = useState([]);
  const [lineColors, setLineColors] = useState([]);

  useEffect(() => {
    if (prices && prices.length !== lineColors.length) {
      const newColors = generateRandomColors(prices.length);
      setLineColors(newColors);
    }
  }, [prices, lineColors]);

  useEffect(() => {
    const fetchData = () => {
      fetch("http://localhost:8000/api/get_stocks/")
        .then((response) => response.json())
        .then((data) => {
          setPrices(data);
        });
    };
  
    fetchData();
  
    const interval = setInterval(() => {
      fetchData();
    }, 30000);
  
    return () => clearInterval(interval);
  }, []);

  const generateRandomColors = (numColors) => {
    const colors = [];
    for (let i = 0; i < numColors; i++) {
      const r = Math.floor(Math.random() * 256);
      const g = Math.floor(Math.random() * 256);
      const b = Math.floor(Math.random() * 256);
      colors.push(`${r}, ${g}, ${b}`);
    }
    return colors;
  };

  return (
    <div>
      <h2>Stock & Crypto Price Charts</h2>
      {prices && <LineCharts data={prices} lineColors={lineColors} />}
    </div>
  );
}

export default ChartContainer;
