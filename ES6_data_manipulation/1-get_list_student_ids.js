// 1-get_list_student_ids.js
export default function getListStudentIds(list) {
  if (!Array.isArray(list)) return [];
  return list.map((student) => student.id);
}
