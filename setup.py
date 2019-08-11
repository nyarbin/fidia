import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
        name = "fidia",
        author = "Ben Reis",
        author_email = "benjamin.e.reis@gmail.com",
        description = "IRS e-file utility",
        long_description = long_description,
        long_description_content_type="text/markdown",
        packages = setuptools.find_packages(),
        classifiers=[ #TODO finish classifiers
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
            "Operating System :: ::",
            ],
        )
