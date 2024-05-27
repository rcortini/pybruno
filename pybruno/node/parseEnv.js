const fs = require('fs');
const parseEnv = require('./envToJson');

const inputFilePath = process.argv[2];

fs.readFile(inputFilePath, 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading file:', err);
        process.exit(1);
    }
    const result = parseEnv(data);
    console.log(JSON.stringify(result));
});