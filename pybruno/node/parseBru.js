const fs = require('fs');
const parseBRU = require('./bruToJson');

const inputFilePath = process.argv[2];

fs.readFile(inputFilePath, 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading file:', err);
        process.exit(1);
    }
    const result = parseBRU(data);
    console.log(JSON.stringify(result));
});