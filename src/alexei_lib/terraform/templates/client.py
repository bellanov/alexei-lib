"""Terraform Project Template."""


CLIENT = """

/**
Create and manage projects, folders, and their relationships.
*/

##############################################
# Alexei
##############################################

# root
resource "google_folder" "alexei" {
  display_name = "Alexei"
  parent       = google_folder.clients.name
}

# dev
resource "google_folder" "alexei-dev" {
  display_name = "Alexei - Dev"
  parent       = google_folder.alexei.name
}

# test
resource "google_folder" "alexei-qa" {
  display_name = "Alexei - QA"
  parent       = google_folder.alexei.name
}

# prod
resource "google_folder" "alexei-prod" {
  display_name = "Alexei - Prod"
  parent       = google_folder.alexei.name
}


# Project

## Dev
resource "google_project" "alexei-dev" {
  name            = "Alexei - Dev"
  project_id      = "alexei-dev"
  folder_id       = google_folder.alexei-dev.folder_id
  billing_account = data.google_billing_account.acct.id

  labels = {
    "terraformed" : true
    "source" : "bellanov-master-state"
  }
}

## Test
resource "google_project" "alexei-qa" {
  name            = "Alexei - QA"
  project_id      = "alexei-qa"
  folder_id       = google_folder.alexei-qa.folder_id
  billing_account = data.google_billing_account.acct.id

  labels = {
    "terraformed" : true
    "source" : "bellanov-master-state"
  }
}

## Prod
resource "google_project" "alexei-prod" {
  name            = "Alexei - Prod"
  project_id      = "alexei-prod"
  folder_id       = google_folder.alexei-prod.folder_id
  billing_account = data.google_billing_account.acct.id

  labels = {
    "terraformed" : true
    "source" : "bellanov-master-state"
  }
}


# Artifacts

## Dev - releases
resource "google_storage_bucket" "alexei-releases-dev" {
  name          = "releases-tzq74vtfsacaprg"
  location      = "US"
  force_destroy = true
  project       = google_project.alexei-dev.project_id

  labels = {
    "terraformed" : true
    "source" : "bellanov-master-state"
  }
}

# Dev - logs
resource "google_storage_bucket" "alexei-logs-dev" {
  name          = "logs-hmjbvyp8eqyefrh"
  location      = "US"
  force_destroy = true
  project       = google_project.alexei-dev.project_id

  lifecycle_rule {
    condition {
      age = 3
    }
    action {
      type = "Delete"
    }
  }

  labels = {
    "terraformed" : true
    "source" : "bellanov-master-state"
  }
}

## Test - releases
resource "google_storage_bucket" "alexei-releases-qa" {
  name          = "releases-e7hc2mjcf4grgxd"
  location      = "US"
  force_destroy = true
  project       = google_project.alexei-qa.project_id

  labels = {
    "terraformed" : true
    "source" : "bellanov-master-state"
  }
}

# Test - logs
resource "google_storage_bucket" "alexei-logs-qa" {
  name          = "logs-j4tztbeljefbpvo"
  location      = "US"
  force_destroy = true
  project       = google_project.alexei-qa.project_id

  lifecycle_rule {
    condition {
      age = 3
    }
    action {
      type = "Delete"
    }
  }

  labels = {
    "terraformed" : true
    "source" : "bellanov-master-state"
  }
}

## Prod - releases
resource "google_storage_bucket" "alexei-releases-prod" {
  name          = "releases-piclewkjpnv678n"
  location      = "US"
  force_destroy = true
  project       = google_project.alexei-prod.project_id

  labels = {
    "terraformed" : true
    "source" : "bellanov-master-state"
  }
}

# Prod - logs
resource "google_storage_bucket" "alexei-logs-prod" {
  name          = "logs-nfrjp2w3vyrt9xp"
  location      = "US"
  force_destroy = true
  project       = google_project.alexei-prod.project_id

  lifecycle_rule {
    condition {
      age = 3
    }
    action {
      type = "Delete"
    }
  }

  labels = {
    "terraformed" : true
    "source" : "bellanov-master-state"
  }
}

## Cloud Build - Service Accounts

# Dev
resource "google_service_account" "cloudbuild_service_account_dev" {
  project      = google_project.alexei-dev.project_id
  account_id   = "${google_project.alexei-dev.project_id}-cloudbuild"
  display_name = "Cloud Build - Dev"
  description  = "Cloud Build User."
}

# QA
resource "google_service_account" "cloudbuild_service_account_qa" {
  project      = google_project.alexei-qa.project_id
  account_id   = "${google_project.alexei-qa.project_id}-cloudbuild"
  display_name = "Cloud Build - QA"
  description  = "Cloud Build User."
}

# Prod
resource "google_service_account" "cloudbuild_service_account_prod" {
  project      = google_project.alexei-prod.project_id
  account_id   = "${google_project.alexei-prod.project_id}-cloudbuild"
  display_name = "Cloud Build - Prod"
  description  = "Cloud Build User."
}

## Cloud Build - Log / Release Roles

# Dev
resource "google_project_iam_member" "logging_role_dev" {
  project = google_project.alexei-dev.project_id
  role    = "roles/logging.logWriter"
  member  = "serviceAccount:${google_service_account.cloudbuild_service_account_dev.email}"
}

resource "google_project_iam_member" "storage_role_dev" {
  project = google_project.alexei-dev.project_id
  role    = "roles/storage.objectCreator"
  member  = "serviceAccount:${google_service_account.cloudbuild_service_account_dev.email}"
}

"""

OUTPUT = """

Outputs

"""
