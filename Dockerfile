FROM mcr.microsoft.com/azureml/openmpi4.1.0-cuda11.0.3-cudnn8-ubuntu18.04

RUN git clone https://github.com/RosettaCommons/RoseTTAFold && \
    cd RoseTTAFold && \
    #  create conda environment for RoseTTAFold
    conda env create -f RoseTTAFold-linux.yml && \
    # download and install third-party software if you want to run the entire modeling script (run_pyrosetta_ver.sh)
    ./install_dependencies.sh

RUN pip install azureml-defaults azureml-core azureml-telemetry
RUN pip install --ignore-installed ruamel.yaml==0.17.4