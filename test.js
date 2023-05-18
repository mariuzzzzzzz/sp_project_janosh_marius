const sqlite3 = require('sqlite3').verbose();
const { Chart } = require('chart.js');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

async function graph(employee, covid) {
  // Connect to the SQLite database
  const db = new sqlite3.Database('/Users/mariusaffolter/Documents/GitHub/sp_project_janosh_marius/backend_sp_db/Database/project_SP.db');

  // Read data from tables using queries
  const rows1 = await executeQuery(db, "SELECT * FROM Covid_Data");
  const rows2 = await executeQuery(db, "SELECT * FROM SP_Project_Sums");

  // Close the database connection
  db.close();

  // Extract required columns from the result rows
  const dates = rows1.map(row => row.date);
  const employeeList = rows2.map(row => row[employee]);
  const covidList = rows1.map(row => row[covid]);

  // Generate the chart using Chart.js and JSDOM
  const dom = new JSDOM('<!DOCTYPE html><html><body><canvas id="chart"></canvas></body></html>');
  global.document = dom.window.document;

  const ctx = dom.window.document.getElementById('chart').getContext('2d');
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: dates,
      datasets: [
        {
          label: 'Employees',
          data: employeeList,
          backgroundColor: 'blue',
          borderColor: 'blue',
          fill: false,
          yAxisID: 'employees-axis',
        },
        {
          label: 'COVID',
          data: covidList,
          backgroundColor: 'red',
          borderColor: 'red',
          fill: false,
          yAxisID: 'covid-axis',
        },
      ],
    },
    options: {
      title: {
        display: true,
        text: 'COVID and Employees Over Time',
      },
      scales: {
        xAxes: [{
          ticks: {
            autoSkip: true,
            maxTicksLimit: 20,
            maxRotation: 45,
            minRotation: 45,
          },
        }],
        yAxes: [
          {
            id: 'employees-axis',
            position: 'left',
            scaleLabel: {
              display: true,
              labelString: 'Employees',
            },
          },
          {
            id: 'covid-axis',
            position: 'right',
            scaleLabel: {
              display: true,
              labelString: 'COVID',
            },
          },
        ],
      },
    },
  });

  // Output the chart as an image or save it to a file if needed
  console.log(dom.window.document.getElementById('chart').toDataURL());
}

function executeQuery(db, query) {
  return new Promise((resolve, reject) => {
    db.all(query, [], (err, rows) => {
      if (err) {
        reject(err);
      } else {
        resolve(rows);
      }
    });
  });
}

graph(6, 1);
