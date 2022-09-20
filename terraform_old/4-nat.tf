resource "aws_eip" "dev-nat" {
  vpc = true

  tags = {
    Name = "dev-eip"
  }
}

resource "aws_nat_gateway" "dev-nat" {
  allocation_id = aws_eip.dev-nat.id
  subnet_id     = aws_subnet.dev-public-us-east-1a.id

  tags = {
    Name = "dev-nat"
  }

  depends_on = [aws_internet_gateway.dev-igw]
}
