# ml_ops_dabs
Show the DevOps part of MLOps using Github Actions and DABs

# HowTo
1. git clone this project to local
2. git branch dev
3. edit code (url, catalog, model name, ...)
4. create catalog, schema in databricks
5. databricks bundle init
6. databricks bundle deploy
7. databricks bundle run
8. merge to main branch

# Notice
ML runtime 14.3 lts compatible (numpy.core.numeric.ComplexWarning import problem in > 15.4 ML)
