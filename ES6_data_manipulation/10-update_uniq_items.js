// Modify the value of groceries list if value = 1
export default function updateUniqueItems(Map_groceries) {
	if (!(Map_groceries instanceof Map)) {
		throw new TypeError('Cannot process');
	}

	Map_groceries.forEach((value, key) => {
		if (value === 1) {
			Map_groceries.set(key, 100);
		}
});
}
