import setuptools

setuptools.setup(
    name="fiftyone_pipeline_devicedetection",
    version="0.0.1",
    author="51Degrees",
    python_requires='>=2.7',
    packages=["fiftyone_pipeline_devicedetection"],
    install_requires=["fiftyone_pipeline_core", "fiftyone_pipeline_engines", "fiftyone_pipeline_cloudrequestengine"]
)
