export default function hasValuesFromArray(a_Set, a_Array) {
	for (const value of a_Array) {
		if (!a_Set.has(value)) {
			return false
		}
	}
	return true
}
