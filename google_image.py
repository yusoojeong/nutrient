from google_images_download import google_images_download

chromedriver = "./chromedriver_win32/chromedriver.exe"
response = google_images_download.googleimagesdownload()

arguments = {
    'keywords': 'bibimbob',
    'limit': 500,
    'print_urls': True,
}

paths = response.download(arguments)
print(paths)