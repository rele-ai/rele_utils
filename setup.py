import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rele-utils",
    version="0.0.1",
    author="Gal Shalom",
    author_email="gal@rele.ai",
    description="releai utils internal package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rele-ai/ops-utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	install_requires=[
        "<google-auth>;python_version<'<2.0.1>'",
        "<google-cloud>;python_version<'<0.34.0>'",
        "<google-cloud-container>;python_version<'<2.7.1>'",
        "<kubernetes>;python_version<'<2.7.1>'",
    ]
)