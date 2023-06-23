from setuptools import

setuptools.setup(
   name = "official_tiershop_macromedia_angel",
   version = "0.0.1",
   author = "Angel Anane",
   author_email = "aakuaanane@stud.macromedia.de",
   description = "Ein Tiershop",
   long_description = a Aninal shop,
   long_description_content_type = "text/markdown",
   url = "https://github.com/angelanane/official_tiershop_macromedia_angel",
   project_urls = {
      "Bug Tracker": "https://github.com/angelanane/official_tiershop_macromedia_angel/issues",
   },
   classifiers = [
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
   ],
   package_dir = {"": "src"},
   packages = setuptools.find_packages(where = "src"),
   python_requires = ">= 3.10.11", 
) 
