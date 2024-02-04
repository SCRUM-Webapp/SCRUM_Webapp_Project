---
title: Design Decision 1
parent: Design Decisions
nav_order: 1
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

## 01: Bootstrap Modal vs seperate page

### Meta

Status
: Work in progress - **Decided** - Obsolete

Updated
: 08-12-2023

### Problem statement

When creating a new item or editing an old item the user has to see all the fields of the form and change them all in one place. This could either be done by **redirecting** the user to a different page specific for an item or it could be done by showing a **Pop-Up Window** on the same page as he was on before. This would have been done with the help of Bootstrap modals.

### Decision

We decided to opt for the seperate page since it requires less knowledge of JavaScript and AJAX

### Regarded options

+ Using Bootstrap modals with JavaScript
+ Using Bootstrap modals with  HTML/CSS
+ Redirecting the user to a seperate editing page

### Assessment

**Option 1: Using Bootstrap modals with JavaScript**
- Requires knowledge of JavaScript and AJAX technique
- would be more complex
- would be more intuitive for the user since he remains on the same site

**Option 2: Using Bootstrap modals with  HTML/CSS**
- less JavaScript/AJAX knowledge needed
- would require a lot of workarounds
- would then in the end possibly not work very well

**Option 3: Redirecting the user to a seperate editing page**
- no JavaScript/AJAX knowledge needed
- less complex
- might be less intuitive for the user


---