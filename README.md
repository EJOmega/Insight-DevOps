# Insight-DevOps
Project Objective: Auto-scale EC2 instances to provide additional processing resources during peak season for credit card processing.

What is the purpose, and most common use cases?
Financial institutions that process credit card payments constantly testing the transactions per second (TPS) volume their systems can handle in preparation for peak season. Peak season typically kicks off end of Novemeber into January for the holiday season. The most common use case is "JT Enterprises" processes averages 700 TPS non-peak load, and avergae 950 TPS peak season with potential spikes short or sustained spikes of over 1000 TPS. 

Which technologies are well-suited to solve those challenges?
  This is where I'm having some trouble...
    I'm under the impression I'll need Kakfa, EC2, Slack Bot (I can tell to spin up a new server), S3 as a DB(?), some open source product similar to Loadrunner to test load on a server.
    
Proposed architecture
'Loadrunner' server transmitting data to an EC2 instance writing to a DB, as the TPS increases, the Slack bot will auto-scale/provision another EC2 instance to process the additional TPS. 
