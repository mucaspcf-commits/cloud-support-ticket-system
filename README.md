# Cloud Support Ticket System

A Python command-line learning project for managing cloud support tickets.

## Run

Requires Python 3. No external packages are needed.

```sh
python cloud_support.py
```

## Features

- Separate user and support menus
- Tickets for AWS, Azure, Google Cloud, Oracle Cloud, IBM Cloud and Salesforce
- Ticket priorities, status changes, timestamps and support comments
- Unresolved ticket reports and simulated recurring maintenance

## Demo access

Enter any valid email address to use the regular user menu. The support menu uses the example addresses `cloud.support@company.com` and `team.leader@company.com`.

This is an educational demonstration: access is selected by email without password authentication. Tickets remain in memory and are lost when the program closes. Maintenance prints reports; it does not connect to cloud services.
