// Imports
const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const cors = require('cors');
const http = require('http');
const bodyParser = require('body-parser');
const config = require('./config');

// Set up App
const app = express();
app.use(cors());
app.use(express.static('public'));
app.use(bodyParser.json());
const port = process.env.PORT || '3001';
app.set('port', port);

const server = http.createServer(app);

// Create the database connection
let database;
const db = new sqlite3.Database('/Users/mariusaffolter/Documents/GitHub/sp_project_janosh_marius/backend_sp_db/Database/project_SP.db');

// ENDPOINT

app.get('/api', async (req, res) => {
  res.send('Welcome to the Music Database API');
});

// Get all artists

app.get('/api/covid-data', async (req, res) => {
  try {
    // Retrieve all artists from the database
    db.all('SELECT * FROM Covid_Data', (err, rows) => {
      if (err) {
        res.status(500).send({ error: err.message });
      } else {
        res.send(rows);
      }
    });
  } catch (error) {
    res.status(500).send({ error: error.message });
  }
});

// Start the server
server.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});