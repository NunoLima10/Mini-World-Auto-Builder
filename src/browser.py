
import webbrowser
class Browser:
    def __init__(self) -> None:
        self.urls = {
            "Tutorial":"https://www.youtube.com/c/NunoLima10",
            "Online Voxelizer":"https://drububu.com/miscellaneous/voxelizer/?out=obj",
            "YouTube Channel":"https://www.youtube.com/c/NunoLima10",
            "Repository":"https://github.com/NunoLima10/Mini-World-Auto-Builder",
        }
    def open_page(self, url_key: str) -> None:
        url =  self.urls[url_key]
        webbrowser.open_new(url)