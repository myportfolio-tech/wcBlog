resource "aws_vpc" "weknowx" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "weknowx"
  }
}
