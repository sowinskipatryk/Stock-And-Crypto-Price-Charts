import LineChart from "./LineChart";

const LineCharts = (props) => {
  const stockData = props.data;
  const colorBase = props.lineColors;

  return (
    <>
      {stockData.map((stock, id) => {
        const color = `rgba(${colorBase[id]}, 0.6)`; 
        const colorBg = `rgba(${colorBase[id]})`;
        return <LineChart data={stock} key={stock.name} color={color} colorBg={colorBg} />;
      })}
    </>
  );
};

export default LineCharts;
