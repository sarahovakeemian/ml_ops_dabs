# ml_ops_dabs
Show the DevOps part of MLOps using Github Actions and DABs
Forked from [sarahovakeemian](https://github.com/sarahovakeemian/ml_ops_dabs) repository

# Prerequisites
1. [Install databricks cli](https://docs.databricks.com/en/dev-tools/cli/install.html)
2. [Get databricks PAT](https://docs.databricks.com/en/dev-tools/auth/pat.html)
3. [PAT authentication](https://docs.databricks.com/en/dev-tools/cli/authentication.html#databricks-personal-access-token-authentication)
4. Set environment secrets in Github > Environments > Environments Secrets, you should make two environments - dev and prod
   * name: DATABRICKS_TOKEN, value: PAT

# Structure
<pre>
ML_OPS_DABS/
├── .github/workflows/
│   ├── dev-databricks-infra-ci-cd.yaml
│   └── prod-databricks-infra-ci-cd.yaml
├── databricks_infra/
│   └── deploy-model-pipeline.yml
├── notebooks/
│   ├── config/
│   │   └── __init__.py
│   ├── serving/
│   │   ├── create_endpoint.py
│   │   └── utils.py
│   ├── workflow_configs/
│   │   ├── endpoint_perms.yaml
│   │   └── model_deployment.yaml
│   ├── download_artifact.py
│   ├── create_serving_endpoint.py
│   ├── model_deployment.py
│   └── model_training.py
├── databricks.yml
└── README.md
</pre>

* databricks.yml: bundle name, infra config inclusion, target workspace
* .github/workflows/ : github action files
    * dev-databricks-infra-ci-cd.yaml : Action for dev branch (only validate, as frequent push to dev, deploy everytime is not required)
    * prod-databricks-infra-ci-cd.yaml : Action for prod branch (deploy and run)
* databricks_infra : databricks.yml includes this
    * deploy-model-pipeline.yml : Cluster, permission, job metadata
* notebooks : model related codes
    * config : definition of dataclass generated from environment yaml files
       * \_\_init\_\_.py : Model metadata creation
    * serving : serving related codes
       * create_endpoint.py : create or update model serving endpoint
       * util.py : credential related
    * workflow_configs : Config directory
       * endpoint_perms.yaml : permission
       * model_deployment.yaml : model metadata
    * download_artifact.py : download model artifacts if it is prod environment
    * create_serving_endpoint.py : create model endpoint
    * model_deployment.py : copy model from dev if it is prod environment
    * model_training.py : training code

# HowTo
1. [local]: git clone this project to local
2. [local]: git branch dev
3. [local]: edit code (url, catalog, model name, ...)
   * databricks.yml: change endpoint for dev, prod
   * deploy-model-pipeline.yml (if it is required)
   * workflow_configs/*
4. [databricks]: create catalog, schema in databricks as written in 3.
5. [local]: databricks bundle init --profile {profile_name}
6. [local]: databricks bundle deploy --profile {profile_name}
7. [databricks]: Go to the bundle workspace and run "model_training.py" using same interactive cluster as defined in deploy-model-pipeline.yml
8. [databricks]: Go to "Model" menu, and set alias "champion"
7. [local]: databricks bundle run --profile {profile_name}
8. [local or databricks or github]: merge to main branch

# Notice
numpy==1.26.4 is required

# Contact
stefano.jang@databricks.com

# Disclaimer
Please note that all projects in the /Stefano-Jang github account are provided for your exploration only, and are not formally supported by Databricks with Service Level Agreements (SLAs). They are provided AS-IS and we do not make any guarantees of any kind. Please do not submit a support ticket relating to any issues arising from the use of these projects.

Any issues discovered through the use of this project should be filed as GitHub Issues on the Repo. They will be reviewed as time permits, but there are no formal SLAs for support.