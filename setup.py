from setuptools import setup, find_packages

setup(
    name="folder_cleaner",                    # Name of your package/project
    version="0.1.0",                          # Initial version of your package
    description="A tool for organizing and cleaning up folders",  # Short description
    long_description=open("README.md").read(),  # Long description (typically from README)
    long_description_content_type="text/markdown",  # Format of the long description
    author="Your Name",                       # Your name
    author_email="your.email@example.com",    # Your email
    url="https://github.com/yourusername/folder_cleaner",  # Project URL
    packages=find_packages(),                 # Automatically find package directories
    install_requires=[
        "python-dotenv>=0.21.0",              # Example dependency (adjust as needed)
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",                  # Minimum Python version required
    entry_points={
        "console_scripts": [
            "folder-cleaner=folder_cleaner.main:main",  # CLI command (if applicable)
        ],
    },
)