var chart = LightweightCharts.createChart(document.getElementById('chart'), {
	width: 1000,
  	height: 500,
	layout: {
		backgroundColor: '#000000',
		textColor: 'rgba(255, 255, 255, 0.9)',
	},
	grid: {
		vertLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
		horzLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
	},
	crosshair: {
		mode: LightweightCharts.CrosshairMode.Normal,
	},
	priceScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
	timeScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
		timeVisible: true,
		secondsVisible: false,
	},
});

var candleSeries = chart.addCandlestickSeries({
	upColor: '#00ff00',
	downColor: '#ff0000', 
	borderDownColor: 'rgba(255, 144, 0, 1)',
	borderUpColor: 'rgba(255, 144, 0, 1)',
	wickDownColor: 'rgba(255, 144, 0, 1)',
	wickUpColor: 'rgba(255, 144, 0, 1)',
});

fetch('http://127.0.0.1:5000/history')
	.then((r) => r.json())
	.then((response) => {
		console.log(response);
		candleSeries.setData(response);
	})