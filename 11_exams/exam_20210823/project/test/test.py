#from project.library import Library

from unittest import TestCase, main

from project.library import Library
#from library import Library


class LibraryTests(TestCase):
    lib_name = "New York Lib"

    def setUp(self) -> None:
        self.actual_library = Library(self.lib_name)

    def test_init__with_valid_string__expect_instance(self):
        self.assertEqual(self.lib_name, self.actual_library.name)
        self.assertEqual({}, self.actual_library.readers)
        self.assertEqual({}, self.actual_library.books_by_authors)

    def test_init__with_empty_string__expect_value_error(self):
        with self.assertRaises(ValueError) as ex:
            actual_library = Library("")
        expected_error = "Name cannot be empty string!"
        self.assertEqual(expected_error, str(ex.exception))

    def test_add_book_with_book_author_not_in_dict__expect_to_be_added(self):
        author = "Ivan Vasov"
        title = "Pod igoto"
        self.actual_library.add_book(author, title)

        self.assertEqual({author: [title]}, self.actual_library.books_by_authors)

    def test_add_book__with_author_in_list__expect_book_added_to_author_list(self):
        author = "Ivan Vasov"
        title1 = "Borba"
        title2 = "Pod igoto"

        self.actual_library.add_book(author, title1)
        self.actual_library.add_book(author, title2)
        self.assertEqual(2, len(self.actual_library.books_by_authors[author]))
        self.assertEqual(1, len(self.actual_library.books_by_authors))
        self.assertTrue(title2 in self.actual_library.books_by_authors[author])

    def test_add_book__with_book_in_dict_expect_dict_not_changed(self):
        author = "Ivan Vasov"
        title = "Pod igoto"
        self.actual_library.add_book(author, title)
        self.actual_library.add_book(author, title)

        self.assertEqual(1, len(self.actual_library.books_by_authors[author]))

    def test_add_reader__with_reader_not_in_dict__expect_reader_added(self):
        reader_name = "John"

        self.actual_library.add_reader(reader_name)

        self.assertEqual(1, len(self.actual_library.readers))
        self.assertEqual([], self.actual_library.readers[reader_name])
        self.assertTrue(reader_name in self.actual_library.readers)

    def test_add_reader__with_reader_already_in_the_dict__expect_string(self):
        reader_name = "John"

        self.actual_library.add_reader(reader_name)

        actual_result = self.actual_library.add_reader(reader_name)
        expected_string = f"{reader_name} is already registered in the {self.lib_name} library."

        self.assertEqual(expected_string, actual_result)
        self.assertEqual(1, len(self.actual_library.readers))
        self.assertEqual([], self.actual_library.readers[reader_name])
        self.assertTrue(reader_name in self.actual_library.readers)

    def test_rent_book__with_valid_book_and_valid_reader__expect_book_added_to_reader_list_and_removed_from_books_list(self):
        author = "Ivan Vasov"
        title = "Pod igoto"
        self.actual_library.add_book(author, title)
        reader_name = "John"
        self.actual_library.add_reader(reader_name)
        self.actual_library.rent_book(reader_name, author, title)

        self.assertEqual(0, len(self.actual_library.books_by_authors[author]))
        self.assertEqual([{author: title}], self.actual_library.readers[reader_name])

    def test_rent_book__with_reader_not_in_readers_dict__expect_string(self):
        author = "Ivan Vasov"
        title = "Pod igoto"
        self.actual_library.add_book(author, title)
        reader_name = "John"
        self.actual_library.add_reader(reader_name)

        reader_name_2 = "Steve"
        actual_result = self.actual_library.rent_book(reader_name_2, author, title)
        expected_result = f"{reader_name_2} is not registered in the {self.lib_name} Library."
        self.assertEqual(expected_result, actual_result)

        self.assertEqual(1, len(self.actual_library.books_by_authors[author]))
        self.assertEqual([], self.actual_library.readers[reader_name])

    def test_rent_book__with_author_not_in_book_dict__expect_string(self):
        author = "Ivan Vasov"
        title = "Pod igoto"
        self.actual_library.add_book(author, title)
        reader_name = "John"
        self.actual_library.add_reader(reader_name)

        wanted_author = "Lev Tolstoy"
        actual_result = self.actual_library.rent_book(reader_name, wanted_author, title)
        expected_result = f"{self.lib_name} Library does not have any {wanted_author}'s books."
        self.assertEqual(expected_result, actual_result)

        self.assertEqual(1, len(self.actual_library.books_by_authors[author]))
        self.assertEqual([], self.actual_library.readers[reader_name])

    def test_rent_book__with_title_not_in_book_dict__expect_string(self):
        author = "Ivan Vasov"
        title = "Pod igoto"
        self.actual_library.add_book(author, title)
        reader_name = "John"
        self.actual_library.add_reader(reader_name)

        wanted_title = "Borba"
        actual_result = self.actual_library.rent_book(reader_name, author, wanted_title)
        expected_result = f"""{self.lib_name} Library does not have {author}'s "{wanted_title}"."""
        self.assertEqual(expected_result, actual_result)

        self.assertEqual(1, len(self.actual_library.books_by_authors[author]))
        self.assertEqual([], self.actual_library.readers[reader_name])


if __name__ == "__main__":
    main()
