terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" { 
  region     = "us-west-2"
}

resource "aws_instance" "ksdc" {
  ami           = "ami-830c94e3"
  instance_type = "t2.micro"

  tags = {
    Name = "Terraform"
  }
}
output "all_tags" {
  value = aws_instance.ksdc.tags_all
}
