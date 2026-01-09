const fs = require('fs');

function countStudents(path) {
	return new Promise((resolve, reject) => {

	fs.readFile(path, 'utf8', (err, csvFile) => {
		if (err) {
			reject(new Error('Cannot load the database'));
			return;
		}

	const data = csvFile.split('\n').filter((line) => line.trim() !== '');


	//remove the header in CSV and empty line
	const body = data.slice(1);

	console.log(`Number of students: ${body.length}`);

	const fields = {};

	for (const student of body) {
		const parts = student.split(',');
		const firstname = parts[0];
		const field = parts[3];

		if (!fields[field]) {
			fields[field] = [];
			fieldOrder.push(field);
		}
		fields[field].push(firstname);
	}

	for (const field in fields) {
		console.log(
			`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`
		);
	}

			resolve();
		});
	});
}

module.exports = countStudents;
