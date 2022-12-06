import { sqlite3 } from 'sqlite3';

export default class DBConnector {
    constructor props = {
        db = db
    }
    sqlite3 = require('sqlite3').verbose();

    // open database in memory
    db = new sqlite3.Database('./database/test.db', sqlite3.OPEN_READWRITE, (err) => {
        if (err) {
            console.error(err.message);
        }
        console.log('Connected to the chinook database.');
    });
}



// close the database connection
db.close((err) => {
  if (err) {
    return console.error(err.message);
  }
  console.log('Close the database connection.');
});