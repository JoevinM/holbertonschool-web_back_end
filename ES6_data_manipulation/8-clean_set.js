// return a string of all the set who match with a specific string
xport default function cleanSet(set, startString) {
	if (startString) {
		const new_array = [];
		for (const value of set) {
			if (value.startsWith(startString)) {
				new_array.push(value.slice(startString.length));
			}
		}
		return new_array.join("-");
	}
		return '';
	}
