import webbrowser


urls = {
    "Online Voxelizer":"https://drububu.com/miscellaneous/voxelizer/?out=obj",
    "YouTube Channel":"https://www.youtube.com/c/NunoLima10",
    "Repository":"https://github.com/NunoLima10/Mini-World-Auto-Builder",
}


def open_page_url(url)-> None:
    webbrowser.open_new(urls[url])