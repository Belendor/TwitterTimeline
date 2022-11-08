
output "public_ec2_ips" {
  value = [
    for instance in aws_instance.main :  join("", ["http://", instance.public_ip])
  ]
}