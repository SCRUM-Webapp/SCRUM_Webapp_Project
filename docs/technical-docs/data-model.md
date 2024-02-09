---
title: Data Model
parent: Technical Docs
nav_order: 3
---

{: .label }
Nicolas

# Data model
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Version 1.0
![version 1.0](/SCRUM_Webapp_Project/assets/images/data_structure_version1.png)

## Version 2.0

### Table Ticket

| Attribute      | Type        | Properties                              |
|----------------|-------------|-----------------------------------------|
| ticket_id      | INTEGER     | PRIMARY KEY, NOT NULL, AUTOINCREMENT    |
| ticket_name    | VARCHAR(80) | NOT NULL                                |
| sprint_number  | INTEGER     |                                         |
| workload       | FLOAT       |                                         |
| description    | TEXT        |                                         |
| ticket_status  | VARCHAR(17) | DEFAULT 'Inbox'                         |
| assigned       | VARCHAR(30) |                                         |
| notes          | TEXT        |                                         |

### Table User

| Attribute | Type        | Properties                              |
|-----------|-------------|-----------------------------------------|
| id        | INTEGER     | PRIMARY KEY, NOT NULL, AUTOINCREMENT    |
| username  | VARCHAR(80) | NOT NULL                                |
| email     | VARCHAR(80) | NOT NULL                                |
| password  | VARCHAR(128)| NOT NULL                                |

