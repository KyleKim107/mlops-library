from mlopslib import MLOpsGCSClient

GCP_KEY_FILE = {
  ## Personal Infos
}



client = MLOpsGCSClient(GCP_KEY_FILE)

client.upload_model(
    bucket_name="mlops-library",
    model_name="nlp-model",
    local_dir_path="../model",
)