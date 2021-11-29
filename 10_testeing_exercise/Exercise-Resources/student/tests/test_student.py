from project.student import Student
from unittest import TestCase, main


class StudentTests(TestCase):
    name = "Hristo"
    courses = {
        "JS": ["online"],
        "Python": ["in class"]
    }

    def setUp(self) -> None:
        self.actual_student = Student(self.name, self.courses)

    def test_init__with_courses__expect_instance(self):
        self.assertEqual(self.name, self.actual_student.name)
        self.assertEqual(self.courses, self.actual_student.courses)

    def test_init__with_no_courses__expect_instance_with_empty_dict(self):
        actual_student = Student(self.name)
        self.assertEqual(self.name, actual_student.name)
        self.assertEqual({}, actual_student.courses)

    def test_enroll__with_existing_course__expect_notes_update(self):
        course = "JS"
        notes = ["level 1"]

        name = "Hristo"
        courses = {
            "JS": ["online"],
            "Python": ["in class"]
        }
        actual_student = Student(name, courses)
        actual_result = actual_student.enroll(course, notes)
        self.assertEqual("Course already added. Notes have been updated.", actual_result)
        [courses[course].append(x) for x in notes]
        self.assertEqual(courses, actual_student.courses)

    def test_enroll__with_new_course_and_adnotes_y__expect_course_added_to_dict(self):
        course = "Go"
        notes = ["level 1"]
        add_course_notes = "Y"
        name = "Hristo"
        courses = {
            "JS": ["online"],
            "Python": ["in class"]
        }
        actual_student = Student(name, courses)

        actual_result = actual_student.enroll(course, notes, add_course_notes)
        self.assertEqual("Course and course notes have been added.", actual_result)
        updated_courses = {
            "JS": ["online"],
            "Python": ["in class"],
            "Go": ["level 1"]
        }
        self.assertEqual(updated_courses, actual_student.courses)

    def test_enroll__with_new_course_and_adnotes_empty_string__expect_course_added_to_dict(self):
        course = "Java"
        notes = ["level 1"]
        add_course_notes = ""

        name = "Hristo"
        courses = {
            "JS": ["online"],
            "Python": ["in class"]
        }
        actual_student = Student(name, courses)

        actual_result = actual_student.enroll(course, notes, add_course_notes)
        self.assertEqual("Course and course notes have been added.", actual_result)

        updated_courses = {
            "JS": ["online"],
            "Python": ["in class"],
            "Java": ["level 1"]
        }
        self.assertEqual(updated_courses, actual_student.courses)

    def test_enroll__with_new_course_and_adnotes_n__expect_course_added_to_dict(self):
        course = "C#"
        notes = ["level 1"]
        add_course_notes = "N"

        name = "Hristo"
        courses = {
            "JS": ["online"],
            "Python": ["in class"]
        }
        actual_student = Student(name, courses)

        actual_result = actual_student.enroll(course, notes, add_course_notes)
        self.assertEqual("Course has been added.", actual_result)
        updated_courses = {
            "JS": ["online"],
            "Python": ["in class"],
            "C#": []
        }
        self.assertEqual(updated_courses, actual_student.courses)

    def test_add_notes__with_course_in_list__expect_notes_added(self):
        course = "Python"
        notes = "level 1"

        name = "Hristo"
        courses = {
            "JS": ["online"],
            "Python": ["in class"]
        }
        actual_student = Student(name, courses)

        actual_result = actual_student.add_notes(course, notes)
        self.assertEqual("Notes have been updated", actual_result)
        updated_courses = {
            "JS": ["online"],
            "Python": ["in class", "level 1"]
        }
        self.assertEqual(updated_courses, actual_student.courses)

    def test_add_notes__with_course_not_in_list__expect_exception(self):
        course = "Go"
        notes = "level 1"
        with self.assertRaises(Exception) as ex:
            self.actual_student.add_notes(course, notes)

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))
        self.assertEqual(self.courses, self.actual_student.courses)

    def test_leave_course__with_course_in_list__expect_course_removed_from_courses(self):
        course = "Python"

        name = "Hristo"
        courses = {
            "JS": ["online"],
            "Python": ["in class"]
        }
        actual_student = Student(name, courses)

        actual_result = actual_student.leave_course(course)
        self.assertEqual("Course has been removed", actual_result)

        updated_courses = {
            "JS": ["online"]
        }
        self.assertEqual(updated_courses, actual_student.courses)

    def test_leave_course__with_course_not_in_list__expect_exception(self):
        course = "Ruby"

        with self.assertRaises(Exception) as ex:
            self.actual_student.leave_course(course)

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
        self.assertEqual(self.courses, self.actual_student.courses)



if __name__ == "__main__":
    main()