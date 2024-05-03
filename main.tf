provider "google" {
  credentials = file("~/gcp-credentials.json")
  project     = "local-passage-419615"
  region      = "us-east1-b"
}

resource "google_container_cluster" "gke_cluster" {
  name     = "moj-klast-gke"
  location = "us-east1-b"

  deletion_protection = false

  node_pool {
    name       = "default-pool"
    node_count = 8

    node_config {
      machine_type = "e2-micro"
      disk_size_gb = 30
    }
  }
}