import setuptools

with open("README.md", "r") as f:
    description = f.read()

setuptools.setup(
    name="smsir-python",
    version="1.0.0",
    author="Mojtaba Akbari",
    author_email="mojtaba.akbari.221b@gmail.com",
    packages=["sms_ir"],
    description="Python Package of SMS.ir Panel ",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/IPeCompany/SmsPanelV2.Python",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[]
)