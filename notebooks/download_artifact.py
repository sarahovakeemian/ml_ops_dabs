# Databricks notebook source
# MAGIC %pip install --upgrade docker
# MAGIC %pip install --upgrade mlflow-skinny[databricks]
# MAGIC
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

import mlflow
from mlflow import MlflowClient
from config import DeployModelConfig, ServingEndpointPermissions

# COMMAND ----------

dbutils.widgets.text("config_path", "workflow_configs/model_deployment.yaml")
dbutils.widgets.text("perms_config_path", "workflow_configs/endpoint_perms.yaml")
dbutils.widgets.text("environment", "dev")
config_path = dbutils.widgets.get("config_path")
perms_config_path = dbutils.widgets.get("perms_config_path")
environment = dbutils.widgets.get("environment")

# COMMAND ----------

cfg = DeployModelConfig.from_yaml(config_path)
cfg

# COMMAND ----------

mlflow.set_registry_uri("databricks-uc")
client = MlflowClient()
model = getattr(cfg, f"{environment}_model")

def get_run_id_by_alias(model_name, alias):
    model_version = client.get_model_version_by_alias(model_name, alias)
    run_id = model_version.run_id
    return run_id

def download_model_artifacts():
    model_name = model.path
    alias = model.model_alias
    target_image_name = f"{model.model_name}_image"
    LOCAL_ARTIFACT_PATH = "../downloaded_artifacts"
    run_id = get_run_id_by_alias(model_name, alias)
    print(f"Run ID: {run_id}")
    artifact_uri = f"runs:/{run_id}/model"
    mlflow.artifacts.download_artifacts(artifact_uri=artifact_uri, dst_path=LOCAL_ARTIFACT_PATH)
    # Dockerization and upload to Cloud Storage or Container Registry
    # TODO

# COMMAND ----------

predecessor_envs = {"prod": "dev"}
if environment != "dev":
    download_model_artifacts()
else:
    # no-op in dev
    print("Running in dev, so nothing to do")
