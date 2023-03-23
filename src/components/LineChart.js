import Chart from "chart.js/auto";
import { Line } from 'react-chartjs-2';
import styles from "./LineChart.module.css";

const LineChart = (props) => {

    const stockPrices = props.data;
    const color = props.color;
    const colorBg = props.colorBg;

    const chartData = {
        labels: stockPrices.date,
        datasets: [{
        label: stockPrices.name,
        data: stockPrices.price,
        backgroundColor: colorBg,
        borderColor: color,
        fill: false,
        }],
    };

  return (
    <div className={styles.chartBox}>
      <Line data={chartData} options={{ maintainAspectRatio: false }} />
    </div>
  );
}


export default LineChart;