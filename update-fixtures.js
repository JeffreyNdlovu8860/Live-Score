import fetch from 'node-fetch';
import fs from 'fs';

const url = 'https://openfootball.github.io/england/2025-26/1-premierleague.json';

async function updateFixtures() {
  const response = await fetch(url);
  const data = await response.json();

  const fixtures = data.matches.slice(0, 7).map(match => ({
    date: match.date,
    team1: match.team1,
    team2: match.team2,
    time: match.time || 'TBD'
  }));

  const jsContent = `const fixtures = ${JSON.stringify(fixtures, null, 2)};`;
  fs.writeFileSync('fixtures.js', jsContent);
  console.log('fixtures.js updated successfully.');
}

updateFixtures();
