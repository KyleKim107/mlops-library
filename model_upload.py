from mlopslib import MLOpsGCSClient

GCP_KEY_FILE = {
  "type": "service_account",
  "project_id": "mlops-projects-456022",
  "private_key_id": "73397d9a1f507285ff262047c03ea8e43d183b0c",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCwIKjvhC6fnG2w\nP1kek2ww6rjvJjjgjbley9VEB4OrStvup0KFawz81Ubp7gzbzaZ54MG0n3LmPFBB\nZURlPJAXG7jdWOdM8LE/oIBq6BNqMpl9KpRz9CjGZj/wIn9whUFkjeDBl+d+vGOR\nlZZtHv2abU4YHkY2Ta56PzzPPjZ8E5RDn+DOpUPITGhbMh6hMB0SQvhycUiPVfax\n6bcP+/2zOb+uV4q5ZVU6vXSbRiwhFTJkPu2g7zJMJIch2Wx6XugTrJax9x1TNMZp\nEve0QeT8Z3BmVKrAfpoc/6RV+4tRVFX7U+StomjBY0r3/ltUVrhSgHIHPIgmG/P0\nU0W6sAhtAgMBAAECggEAIQLmFwp74J+lsXiWIBR6nUqJQg20cGYv3dQvk1IjPCpK\nQZdo8O/JHeRtp6/eCh6n+sUFGXEfTIb2deNgp+brjOE9y4L7y2B7oFTZbPA1n1x/\nh0XBUGBteg41IrGcmD7prEqpWy+5DHiL4wAaEzbRSq39Cqk1+LyjnLcYkzFybdu/\nIM5LnIyJd6ojZUf2+Y8ppFIY+3GYfT+XXR03Fj09kUccnxxEL9UX2d5BpuwKCPpM\nHuSdI4QtWxK9zL2lHFCMdUqjymFFoA/agSDDtaBbxVowSgvdTHwQZoC8uxEBk2r6\nnNvsjU6kOsELIrbZexkExcRPZIoU4UBonbuy8ZuKwQKBgQD2JS7GDo8zr74/77kM\nIYITS/ZbstDhy6jySxCfgUBDLgaBA7GLLjwhzoXV2jtwp1KUyHDxUXCuChSzSN1N\na7MsinDba7ZxutyNxzWdbiUXC9KFPyzj+8TVIwaIERaoFXSJtkx9+r3DO40qW2CO\nPb6HycheSOBt3ldzrQC0/pR4DQKBgQC3LdhKMrKusQPjIr2qOxw1soF6wY2ABDVN\n6fpMQ+r3+t1R0Jd8mQZXLRvMCaswFJoGnKIlXVDLUg4kXfY3S9NIdKFHBepOIyKt\n7PWgFT0xhiB80OQz7Rjz2K1BPr22zXJ8hmqrJWkEZ0nOtjryx74iHdhIlB2c2jtc\nIIKUSs5Z4QKBgQCQdsI8+86QR1UhsVCqDgCJ0suEhi6SVzWQ/v2CoBlXVGv8zG4n\ngbtJHCzwlmTMeWe+auXevC2l98SudNVt2wgN3DLglRc/KKzJiWGuRDcAj6+/BJUU\nOXAMp8HtmhnyDKWZLaU3SzKUox72/SpuUU7B42v16k/OK/Cns6H2mHQLAQKBgQCC\nu5hzFA3MeY9xqti8RqWSeUzJhJvtcpNsgQHfLlXjF8qe2oVTKo+I5ivBimD/1qQ6\n9c0PZ7MC+RQYxmqz+kzXmE2GN+WKUK8ufECtOJtM3hIPorJLkPrPBaRZPWL+tU/x\nKam1beSufN0DR7F4li/Pf4dd/T/JM0NMM/OdzGnLYQKBgBN3dla1iRZ9F6HegmWH\nMEEf+9GE1RvDPDLdpKNg3WoGWRFOE1HeLg4B05DVYrqnaumM030Nkdsb9bdoiuFu\nWw/GzjizNAfVnXKSkRr/J0quoQ65b2dgUhVHJT6WDs4+jrzQlxw5YwO/j6fjHqDH\njYzADISWmMYlIyldJj2a7U7Q\n-----END PRIVATE KEY-----\n",
  "client_email": "mlops-service-account@mlops-projects-456022.iam.gserviceaccount.com",
  "client_id": "112355588665505574695",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/mlops-service-account%40mlops-projects-456022.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}




client = MLOpsGCSClient(GCP_KEY_FILE)

client.upload_model(
    bucket_name="mlops-library",
    model_name="nlp-model",
    local_dir_path="../model",
)