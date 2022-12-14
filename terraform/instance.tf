resource "aws_instance" "main" {
  count = var.ec2_count

  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t2.micro"
  key_name               = aws_key_pair.generated_key.key_name
  subnet_id              = module.vpc.public_subnets[count.index % length(module.vpc.public_subnets)]
  vpc_security_group_ids = [aws_security_group.my-sg.id]
  user_data = templatefile("${path.module}/instance-script.sh", {
    file_content = "main online"
  })

  tags = {
    Name = "TwitterTimeline-main"
  }
}