resource "aws_iam_role" "weknowx" {
  name = "eks-cluster-dev-weknowx"

  assume_role_policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "eks.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
POLICY
}

resource "aws_iam_role_policy_attachment" "weknowx-AmazonEKSClusterPolicy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
  role       = aws_iam_role.weknowx.name
}

resource "aws_eks_cluster" "dev-weknowx" {
  name     = "dev-weknowx"
  role_arn = aws_iam_role.weknowx.arn

  vpc_config {
    subnet_ids = [
      aws_subnet.dev-private-us-east-1a.id,
      aws_subnet.dev-private-us-east-1b.id,
      aws_subnet.dev-public-us-east-1a.id,
      aws_subnet.dev-public-us-east-1b.id
    ]
  }

  depends_on = [aws_iam_role_policy_attachment.weknowx-AmazonEKSClusterPolicy]

}
