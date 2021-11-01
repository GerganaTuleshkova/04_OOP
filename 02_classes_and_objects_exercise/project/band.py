from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for album_object in self.albums:
            if album_object.name == album_name and album_object.published:
                return "Album has been published. It cannot be removed."
            if album_object.name == album_name:
                self.albums.remove(album_object)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        resulting_string = f"Band {self.name}"
        for album_object in self.albums:
            resulting_string += f"\n{album_object.details()}"
        return resulting_string

