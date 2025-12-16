//Filters an array of student objects by a given city.
export default function getStudentsByLocation(array_students, city) {
	return array_students.filter(student => student.location === city)
}
