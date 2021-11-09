from math import ceil


class PhotoAlbum:
    _photos_per_page = 4
    _page_separation = 11

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = []
        for r_i in range(self.pages):
            self.photos.append([])

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / cls._photos_per_page)
        return cls(pages)

    def add_photo(self, label: str):
        for page_i in range(self.pages):
            if len(self.photos[page_i]) < self._photos_per_page:
                self.photos[page_i].append(label)
                return f"{label} photo added successfully on page {page_i + 1} slot {len(self.photos[page_i])}"
        return "No more free slots"

    def display(self):
        resulting_string = ""
        for page_i in range(self.pages):

            resulting_string += "-" * self._page_separation + "\n"
            resulting_string += f"{('[] ' * len(self.photos[page_i])).strip()}\n"
        resulting_string += "-" * self._page_separation
        return resulting_string


import unittest


class TestsPhotoAlbum(unittest.TestCase):
    def test_init_creates_all_attributes(self):
        album = PhotoAlbum(2)
        self.assertEqual(album.pages, 2)
        self.assertEqual(album.photos, [[], []])

    def test_from_photos_should_create_instace(self):
        album = PhotoAlbum.from_photos_count(12)
        self.assertEqual(album.pages, 3)
        self.assertEqual(album.photos, [[], [], []])

    def test_add_photo_with_no_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.add_photo("prom")
        self.assertEqual(result, "No more free slots")

    def test_add_photo_with_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        self.assertEqual(album.photos, [['baby', 'first grade', 'eight grade', 'party with friends']])

    def test_display_with_one_page(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.display().strip()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------")

    def test_display_with_three_pages(self):
        album = PhotoAlbum(3)
        for _ in range(8):
            album.add_photo("asdf")
        result = album.display().strip()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n[] [] [] []\n-----------\n\n-----------")


if __name__ == "__main__":
    unittest.main()