// Creates an object using a dynamic property name for the department
export default function createEmployeesObject(departmentName, employees) {
return {
	[departmentName]: employees,
};
}
