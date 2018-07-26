# Insight-DevOps
Project Objective: Auto-scale Kafka consumers to provide additional processing resources during peak season for credit card processing.

What is the purpose, and most common use cases?
Financial institutions that process credit card payments constantly have to certify that their environments can support high   transactions per second (TPS) volumes, and potential burts during peak season. Peak season typically kicks off end of Novemeber   into January for the holiday season. The most common use case is "JT Enterprises" processes increasing TPS throughout a day during peak season.

Which technologies are well-suited to solve those challenges?
This is subject to change, however I'd like to use a combination Kakfa, AWS-EC2, AWS-S3, Python, and a MySQL database.
    
Proposed architecture
Python scripts acting like Kafka producers will be staggered transmitting data to an EC2 instance writing to a DB, as the TPS increases, additional Kafka consumers will be provisioned in the consumer group in order process the additional transactional load.
