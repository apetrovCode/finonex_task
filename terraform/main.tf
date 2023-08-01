provider "aws" {
  region  = "eu-central-1" 
}

resource "aws_instance" "k8s_node" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "K8sSingleNode"
  }
}

output "ec2_ip" {
  value = aws_instance.k8s_node.public_ip
}

