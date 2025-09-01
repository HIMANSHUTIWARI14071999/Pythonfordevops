# Pythonfordevops
This project demonstrates how to automate the creation and management of AWS S3 buckets and objects using Python wrappers around the AWS SDK (Boto3). The wrapper functions simplify common S3 operations like creating buckets, uploading files, and managing objects, making it easier to integrate cloud storage tasks into automation workflows.

# AWS S3 Automation with Python SDK (Wrappers) 🚀

This project demonstrates how to create and manage **AWS S3 buckets and objects** using **Python**.  
It uses the **AWS SDK for Python (Boto3)**, wrapped inside reusable Python functions, to simplify cloud automation tasks.  

---

## ✨ Features
- Create new **S3 buckets** in specific regions  
- Upload and manage **objects (files)** in buckets  
- Wrapper functions for cleaner and reusable AWS interactions  
- Error handling and validation included  

---

## 🛠️ Prerequisites
- Python 3.8+  
- AWS account with programmatic access (Access Key & Secret Key)  
- AWS CLI configured or credentials stored in `~/.aws/credentials`  
- Install dependencies:  

```bash
pip install boto3
