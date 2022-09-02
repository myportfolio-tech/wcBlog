
# Private Subnet 1
resource "aws_subnet" "private-us-east-1a" {
  vpc_id            = aws_vpc.weknowx.id
  cidr_block        = "10.0.0.0/19"
  availability_zone = "us-east-1a"

  tags = {
    "Name"                            = "weknowx-private-us-east-1a"
    "kubernetes.io/role/internal-elb" = "1"
    "kubernetes.io/cluster/demo"      = "owned"
  }
}

# Private Subnet 2
resource "aws_subnet" "private-us-east-1b" {
  vpc_id            = aws_vpc.weknowx.id
  cidr_block        = "10.0.32.0/19"
  availability_zone = "us-east-1b"

  tags = {
    "Name"                            = "weknowx-private-us-east-1b"
    "kubernetes.io/role/internal-elb" = "1"
    "kubernetes.io/cluster/demo"      = "owned"
  }
}

# Public Subnet 1
resource "aws_subnet" "public-us-east-1a" {
  vpc_id                  = aws_vpc.weknowx.id
  cidr_block              = "10.0.64.0/19"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true

  tags = {
    "Name"                       = "weknowx-public-us-east-1a"
    "kubernetes.io/role/elb"     = "1"
    "kubernetes.io/cluster/demo" = "owned"
  }
}

# Public Subnet 1
resource "aws_subnet" "public-us-east-1b" {
  vpc_id                  = aws_vpc.weknowx.id
  cidr_block              = "10.0.96.0/19"
  availability_zone       = "us-east-1b"
  map_public_ip_on_launch = true

  tags = {
    "Name"                       = "weknowx-public-us-east-1b"
    "kubernetes.io/role/elb"     = "1"
    "kubernetes.io/cluster/demo" = "owned"
  }
}
