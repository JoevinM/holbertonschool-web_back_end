// Returns an array of student ids
export default function getListStudentIds(array_students) {
	if (!Array.isArray(array_students)) {
		return [];
	}

	return 	array_students.map((banana)=>banana.id);
}
