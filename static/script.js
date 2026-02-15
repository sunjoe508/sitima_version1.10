let barChart, pieChart;

async function scanDevices() {
    const response = await fetch("/scan");
    const devices = await response.json();

    const container = document.getElementById("deviceContainer");
    container.innerHTML = "";

    if (devices.length === 0) {
        container.innerHTML = "<p>No devices detected.</p>";
        return;
    }

    let labels = [], powerData = [], costData = [], typeCount = {};

    devices.forEach(device => {
        const div = document.createElement("div");
        div.className = "device-card";
        div.innerHTML = `
            <h3>${device.hostname}</h3>
            <p>IP: ${device.ip}</p>
            <p>Type: ${device.type}</p>
            <p>Power: ${device.estimated_power} W</p>
            <p>Daily kWh: ${device.daily_kwh}</p>
            <p>Daily Cost: ${device.daily_cost} KES</p>
        `;
        container.appendChild(div);

        labels.push(device.hostname);
        powerData.push(device.estimated_power);
        costData.push(device.daily_cost);

        typeCount[device.type] = (typeCount[device.type] || 0) + 1;
    });

    // Destroy old charts
    if(barChart) barChart.destroy();
    if(pieChart) pieChart.destroy();

    // Bar chart (Power)
    const barCtx = document.getElementById("powerBarChart").getContext("2d");
    barChart = new Chart(barCtx, {
        type:'bar',
        data:{ labels, datasets:[{label:'Power (W)', data:powerData, backgroundColor:'rgba(34,197,94,0.7)'}] },
        options:{ responsive:true, scales:{ y:{ beginAtZero:true } } }
    });

    // Pie chart (Type Distribution)
    const pieCtx = document.getElementById("powerPieChart").getContext("2d");
    pieChart = new Chart(pieCtx, {
        type:'pie',
        data:{
            labels: Object.keys(typeCount),
            datasets:[{ label:'Device Types', data:Object.values(typeCount),
                        backgroundColor:['#22c55e','#facc15','#3b82f6','#f43f5e','#8b5cf6'] }]
        },
        options:{ responsive:true }
    });

    updateHistory();
}

async function updateHistory() {
    const response = await fetch("/history");
    const history = await response.json();
    const ul = document.getElementById("historyList");
    ul.innerHTML = "";

    history.forEach(scan => {
        const li = document.createElement("li");
        li.textContent = `${scan.timestamp} - ${scan.devices.length} devices`;
        ul.appendChild(li);
    });
}

function downloadCSV() {
    window.location.href = "/download";
}

function toggleTheme() {
    document.body.classList.toggle("dark");
    document.body.classList.toggle("light");
}

// Auto-refresh every 10s
setInterval(scanDevices, 10000);
