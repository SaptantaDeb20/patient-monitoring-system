let timeIndex = 0;
let demoInterval = null;

const hrData = [];
const spo2Data = [];
const tempData = [];
const labels = [];

// --------- Charts ----------
const hrChart = new Chart(document.getElementById("hrChart"), {
  type: "line",
  data: {
    labels: labels,
    datasets: [
      {
        label: "Heart Rate (bpm)",
        data: hrData,
        borderColor: "red",
        tension: 0.3,
      },
    ],
  },
});

const spo2Chart = new Chart(document.getElementById("spo2Chart"), {
  type: "line",
  data: {
    labels: labels,
    datasets: [
      {
        label: "SpO₂ (%)",
        data: spo2Data,
        borderColor: "green",
        tension: 0.3,
      },
    ],
  },
});

const tempChart = new Chart(document.getElementById("tempChart"), {
  type: "line",
  data: {
    labels: labels,
    datasets: [
      {
        label: "Temperature (°C)",
        data: tempData,
        borderColor: "orange",
        tension: 0.3,
      },
    ],
  },
});

// --------- Send Data ----------
function sendData() {
  const data = {
    patient_id: parseInt(document.getElementById("patient_id").value),
    time_step: timeIndex,
    heart_rate: parseFloat(document.getElementById("heart_rate").value),
    spo2: parseFloat(document.getElementById("spo2").value),
    temperature: parseFloat(document.getElementById("temperature").value),
    scenario: "live",
  };

  fetch("/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  })
    .then((res) => res.json())
    .then((result) => {
      const alertSound = document.getElementById("alertSound");

      if (result.hybrid_alert) {
        alertSound.pause(); // reset sound
        alertSound.currentTime = 0;
        alertSound.play().catch((err) => {
          console.log("Audio blocked:", err);
        });
      }

      // -------- Update Charts --------
      labels.push(timeIndex);
      hrData.push(data.heart_rate);
      spo2Data.push(data.spo2);
      tempData.push(data.temperature);

      hrChart.update();
      spo2Chart.update();
      tempChart.update();

      timeIndex++;

      // -------- Alert UI --------
      let alertClass = result.hybrid_alert ? "alert-danger" : "alert-success";
      let alertText = result.hybrid_alert
        ? "⚠️ ALERT: Patient at Risk"
        : "✅ Patient Stable";

      document.getElementById("result").innerHTML = `
            <div class="alert ${alertClass} shadow">
                <h4>${alertText}</h4>
                <p><strong>Rule Alert:</strong> ${result.rule_alert}</p>
                <p><strong>ML Anomaly:</strong> ${result.ml_anomaly}</p>
                <p><strong>Hybrid Decision:</strong> ${result.hybrid_alert}</p>
            </div>
        `;
    });
}

function startDemo() {
  if (demoInterval !== null) return; // prevent multiple starts

  demoInterval = setInterval(() => {
    // Generate semi-random vitals
    const hr = 70 + Math.random() * 40;
    const spo2 = 92 + Math.random() * 6;
    const temp = 36.5 + Math.random() * 2;

    document.getElementById("heart_rate").value = hr.toFixed(0);
    document.getElementById("spo2").value = spo2.toFixed(0);
    document.getElementById("temperature").value = temp.toFixed(1);

    sendData();
  }, 5000); // every 5 seconds
}
