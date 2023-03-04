terraform {
  required_version = ">= 0.12"
}

# CONFIGURE OUR AWS CONNECTION


provider "aws" {
  region = "ap-northeast-1"
}
terraform {
  backend "s3"{
  region = "ap-northeast-1"
  bucket = "rs-s3bucket"
  key = "table/backend/terraform.ifstate"
  dynamodb_table = "table"
}
}
# CREATE THE S3 BUCKET


resource "aws_s3_bucket" "s3" {
  # With account id, this S3 bucket names can be *globally* unique.
  bucket = "rs-s3bucket"

  tags = {
    Name = "rs-s3bucket"
  }
}

# ------------------------------------------------------------------------------
# CREATE THE DYNAMODB TABLE
# ------------------------------------------------------------------------------

resource "aws_dynamodb_table" "table" {
  name         = "table"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }
}
