// Updates student grades by city using filter and map

export default function updateStudentGradeByCity(studentlist, city, newgrades) {
  return studentlist
    .filter(student => student.location === city)
    .map(student => {
      const gradefound = newgrades.find(
        item => item.studentId === student.id
      );

      return {
        ...student,
        grade: gradefound ? gradefound.grade : 'N/A',
      };
    });
}
