# Insight-DevOps
Project Objective: Auto-scale AWS EC2 and Kafka brokers to provide additional processing resources during peak season for credit card processing. 

What is the purpose, and most common use cases?
Financial institutions that process credit card payments rely on legacy platforms (i.e. NonStop and Mainframe) to do their backend core-data processing. Despite these platforms being mature and reliable, they have a higher total cost of ownership, and tend to be underutilized outside of peak season. I wanted to explore how an AWS Cloud model would react to variable workloads forcing the environment to expand and contract. The expectation is, with a Cloud model that can expand and contract, the business unit be able to predict workload and adopt better demand planning practices which would decrease technology spending.

Which technologies are well-suited to solve those challenges?
I utilized:
Terraform to build my core EC2 nodes. 
Apache Kafka and Zookeeper to manage the broker resources.
Python to create Kafka Producer and Consumer scripts.
AWS Cloudwatch to monitor and alarm on CPU utilization.
AWS Auto-Scaling Groups that expand and contract infrastructure when AWS Cloudwatch alarms have been triggered.
    
Proposed architecture
Python scripts located on separate EC2 instances will act as Kafka producers and consumers that will send data through a Zookeeper/Kafka broker cluster. As the CPUs are stressed, additional brokers created from a Kafka AMI will be integrated into the cluster. The leading Zookeeper will then redistribute topics amongst the available brokers, and will redistribute topics when the additional brokers have been terminated.
