# Databricks notebook source
# MAGIC %pip install --upgrade docker
# MAGIC %pip install --upgrade mlflow-skinny[databricks]
# MAGIC
# MAGIC dbutils.library.restartPython()
# MAGIC
# MAGIC import mlflow
# MAGIC from mlflow import MlflowClient
# MAGIC
# MAGIC mlflow.set_registry_uri("databricks-uc")
# MAGIC client = MlflowClient()
# MAGIC
# MAGIC def get_run_id_by_alias(model_name, alias):
# MAGIC     model_version = client.get_model_version_by_alias(model_name, alias)
# MAGIC     run_id = model_version.run_id
# MAGIC     return run_id
# MAGIC
# MAGIC model_name = "uc_stefano_mlops_prod.ml_ops_dabs.iris_model"
# MAGIC alias = "champion"
# MAGIC target_image_name = "iris_model_image"
# MAGIC LOCAL_ARTIFACT_PATH = "./downloaded_artifacts"
# MAGIC run_id = get_run_id_by_alias(model_name, alias)
# MAGIC print(f"Run ID: {run_id}")
# MAGIC
# MAGIC artifact_uri = f"runs:/{run_id}/model"
# MAGIC
# MAGIC mlflow.artifacts.download_artifacts(artifact_uri=artifact_uri, dst_path=LOCAL_ARTIFACT_PATH)
# MAGIC
# MAGIC # Dockerization and upload to Cloud Storage or Container Registry
# MAGIC # TODO
