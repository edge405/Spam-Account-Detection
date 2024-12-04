document.getElementById("generate-btn").addEventListener("click", async () => {
  const spinner = document.getElementById("loading-spinner");
  spinner.classList.add("active"); // Show spinner

  try {
    const response = await fetch("/generate", { method: "POST" });
    const data = await response.json();

    // Render Tables
    renderTable("all-data", data.all_data);
    renderTable("human-data", data.human_data);
    renderTable("bot-data", data.bot_data);
  } catch (error) {
    console.error("Error fetching data:", error);
    alert("Failed to generate data.");
  } finally {
    spinner.classList.remove("active"); // Hide spinner
  }
});

function renderTable(containerId, data) {
  const container = document.getElementById(containerId);
  container.innerHTML = ""; // Clear any existing content

  if (data.length === 0) {
    container.innerHTML = "<p>No data available.</p>";
    return;
  }

  const table = document.createElement("table");
  table.className = "table table-striped";
  const thead = document.createElement("thead");
  const tbody = document.createElement("tbody");

  // Add headers
  let headers = Object.keys(data[0]); // Include all keys from the first row
  // Ensure 'index' column is the first header
  headers = [
    "index",
    "label",
    ...headers.filter((header) => header !== "index" && header !== "label"),
  ];

  const headerRow = document.createElement("tr");
  headers.forEach((header) => {
    const th = document.createElement("th");
    if (header === "label") {
      th.textContent = "Predicted Label"; // Rename "label" header
    } else if (header === "index") {
      th.textContent = "Index"; // Rename "index" header
    } else {
      th.textContent = header;
    }
    // th.classList.add("table-dark");
    headerRow.appendChild(th);
  });

  thead.appendChild(headerRow);

  // Add rows dynamically
  data.forEach((row) => {
    const tr = document.createElement("tr");

    if (row.label === 0) {
      tr.classList.add("table-success"); // Green for human rows
    } else if (row.label === 1) {
      tr.classList.add("table-danger"); // Red for bot rows
    }

    headers.forEach((header) => {
      const td = document.createElement("td");
      if (header === "label") {
        // Convert the label value to "Human" or "Bot"
        td.textContent = row[header] === 0 ? "Human" : "Bot";
      } else {
        td.textContent = row[header];
      }
      tr.appendChild(td);
    });

    tbody.appendChild(tr);
  });

  table.appendChild(thead);
  table.appendChild(tbody);
  container.appendChild(table);
}
