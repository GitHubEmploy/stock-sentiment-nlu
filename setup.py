from setuptools import setup, find_packages

setup(
    name="stock-sentiment-nlu",
    version="0.1.0",
    description="Stock market sentiment analysis using NLU tokenization and natural language understanding",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Mohit Varikuti",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "nltk>=3.6",
        "requests>=2.25",
        "python-dotenv>=0.19",
    ],
    python_requires=">=3.8",
)
