# RoseTTAFold with Azure Machine Learning
## Introduction
Azure is collaborating with the [Baker Lab](https://www.bakerlab.org/) at the University of Washington to easily run the RoseTTAFold protein folding model using Azure Machine Learning (Azure ML).

For more information on RoseTTAFold, visit the project's [GitHub repo](https://github.com/RosettaCommons/RoseTTAFold) and the [project announcement](https://www.bakerlab.org/index.php/2021/07/15/accurate-protein-structure-prediction-accessible/).

This repo contains three notbooks that will guide you through setting up your Azure ML workspace, submitting jobs for processing, and setting up a batch endpoint for scalable inferencing from the command line interface (CLI) or REST APIs.

**Note:** the RoseTTAFold deployments demonstrated here are not designed to run in production environments. They are is strictly for non-production test environments.

## Notebooks

This repo contains the following notebooks:
- **[1-setup-workspace.ipynb](./1-setup-workspace.ipynb)**
    - Run one-time setup steps to prepare your Azure ML Workspace with the dependency Datasets and a Compute Cluster.
- **[2-run-experiment.ipynb](./2-run-experiment.ipynb)**
    - Run RosettaFold as an Azure ML Experiment. 
    - Create an input file, submit a Run, check status, and get the results.
- **[3-batch-endpoint.ipynb](./3-batch-endpoint.ipynb)**
    - Create a Batch Endpoint that can be called from the Azure CLI or as a REST call. 

## Getting Started

1. Clone this repo:
`git clone https://github.com/microsoft/rosettafold-azureml.git`
2. Open the folder in VS Code (installation instructions [here](https://code.visualstudio.com/), if needed):
`code rosettafold-azureml`
3. Open each notebook and follow along, starting with [1-setup-workspace.ipynb](./1-setup-workspace.ipynb).

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
