---
title: Design Decision 2
parent: Design Decisions
nav_order: 2
---

{: .label }
Nicolas

# Design Decisions
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 02: Incorporating SQLAlchemy into software stack vs sticking with plain SQL statements

### Meta

Status
: Work in progress -**Decided** - Obsolete

Updated
: 02-01-2024

### Problem statement

When interacting with a database we want the process to be as smooth and uncomplicated as possible and the lines of code should be kept to a minimum to increase the overview over what's really important. We already have experience with writing SQL statements but no prior experience with using SQLAlchemy. SQLAlchemy promises a more object oriented approach to CRUD operations which we are familiar with and the amount of code in the resulting workflow is very low. But it will take time to learn the new concepts.

### Decision

We decided to use SQLAlchemy because we like the code clarity and the flexibility it grants us if we want to change the database in the future.

### Regarded options

We regarded two alternative options:

+ Plain SQL statements
+ SQLAlchemy

 Pro SQLAlchemy: | Con SQLAlchemy
 :-- | :-- 
 ✔️ Object oriented programming | ❌ Takes time to learn
 ✔️ Gives us flexibility | ❌ We know how to write SQL statements
 ✔️ No need to write SQL statements | ❌ Could affec database performance (unlikely)
 ✔️ Gives us code clarity 
 ✔️ No need to establish db_con 
 ✔️ Learning a new technology 
 ✔️ Might make up for the time lost initally 
