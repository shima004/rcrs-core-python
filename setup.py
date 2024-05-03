from setuptools import find_packages, setup

# JUST FOR TEST

setup(
    name="rcrs_core",
    version="0.1.0",
    description="RoboCup Rescue Simulation(RCRS Agent Development Library)",
    url="https://github.com/roborescue/rcrs-core-python",
    packages=find_packages(),
    install_requires=["protobuf==4.25.*", "rtree"],
)
