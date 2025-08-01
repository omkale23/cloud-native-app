variable "cluster_name" {
  type    = string
  default = "cloud-native-eks-v2"
}

variable "cluster_version" {
  type    = string
  default = "1.29"
}

variable "region" {
  type    = string
  default = "eu-north-1"
}

variable "vpc_id" {
  type = string
  description = "The VPC in which to deploy the EKS cluster"
}

variable "subnet_ids" {
  type = list(string)
  description = "List of subnet IDs for the EKS worker nodes"
}

variable "node_instance_type" {
  type    = string
  default = "t3.medium"
  description = "EC2 instance type for EKS worker nodes"
}
