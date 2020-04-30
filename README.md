# py_image_crawler


# Dependency 

- Google_images_download

```python

    from google_images_download import google_images_download   #importing the library

    response = google_images_download.googleimagesdownload()   #class instantiation

    arguments = {
        "keywords":"Japan,Japan Photo",
        "limit":100,
        "print_urls":True
    }   #creating list of arguments
    paths = response.download(arguments)   #passing the arguments to the function
    print(paths)   #printing absolute paths of the downloaded images

```

# Python

파이썬이 tool로써는 엄청나게 강력한걸 깨달았지만 진짜 version compatibility에서 맨날 난리가 난다. 가상환경 컴퓨터를 구축해서 사용하지 않는한 production level에서 python을 쓰기는 무리가 아닐까? 근데 진짜 강력한 tool이 많다.  
