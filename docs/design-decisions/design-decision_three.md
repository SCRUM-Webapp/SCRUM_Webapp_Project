---
title: Design Decision 3
parent: Design Decisions
nav_order: 3
---

{: .label }
Vasco

# Design Decisions
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 03: Session management

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 04-02-2024

### Problem statement

When the user successfully logs in his user-ID gets stored in the session. Now the question is: Does the user have to log in again after a certain amount of time or does he not have to log in again.  
This is a question of user experience and security since an expiring session could annoy the user leading him to not use the webapp anymore but at the same time this could also be a safety concern.

### Decision

We decided to let the user stay logged in for 7 days without any interaction with the webapp. We decided a week would be a good compromise since it still doesn't make the user have to log in every day but also still closes sessions that were open and not used for a while. If during that 7 day period the user interacts with our website the 7 day "countdown" gets reset.

### Regarded options

+ Session doesn't expire
+ Session expires after a certain amount of time

### Assessment

| Pro Expiration: | Con Expiration |
 | :-- | :-- | 
 | ✔️ increased window of opportunity for unauthorized access | ❌ user doesn't need to authenticate frequently |
 | ✔️ Might (if actually launched) create problems with regulations | ❌ reduces "friction" for returning users so they can just continue where they stopped last time |
 | ✔️ when session is hijacked there is no limit to how long the hijacker can use the session | ❌ Could make the user more likely to use our product frequently |
 | ✔️ many open sessions increases consumed server ressources | |


---