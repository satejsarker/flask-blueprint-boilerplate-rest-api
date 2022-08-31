terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.20.2"
    }
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}
# Configure the AWS Provider
provider "aws" {
  region = "us-west-2"
}

provider "docker" {}