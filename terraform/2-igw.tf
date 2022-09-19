resource "aws_internet_gateway" "dev-igw" {
  vpc_id = aws_vpc.dev-weknowx.id

  tags = {
    Name = "igw"
  }
}
