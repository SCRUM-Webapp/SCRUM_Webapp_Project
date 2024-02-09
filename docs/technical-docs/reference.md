---
title: Reference
parent: Technical Docs
nav_order: 4
---

{: .label }
Nicolas, Vasco

# Reference documentation
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Section / module

### `index()`

**Route:** `/`

**Methods:** `GET`

**Purpose:** Displays the user's dashboard. Welcomes the user with their username and a different greeting depending on the time.

**Sample output:**

![User_Dashboard](/SCRUM_Webapp_Project/assets/images/User_Dashboard.png)

---

### `login()`

**Route:** `/Login`

**Methods:** `GET`, `POST`

**Purpose:** Renders the login form and handles user authentication.

**Sample output:**

![Login_Screen](/SCRUM_Webapp_Project/assets/images/Login_Screen.png)

---

### `register()`

**Route:** `/Register`

**Methods:** `GET`, `POST`

**Purpose:** Renders the registration form and handles user registration.

**Sample output:**

![Register_Screen](/SCRUM_Webapp_Project/assets/images/Register_Screen.png)

---

### `product_backlog()`

**Route:** `/Product_Backlog`

**Methods:** `GET`

**Purpose:** Renders the product backlog page, displaying tickets categorized into different stages.

**Sample output:**

![Product_Backlog](/SCRUM_Webapp_Project/assets/images/Product_Backlog.png)

---

### `ticket(ticket_id)`

**Route:** `/Ticket/<int:ticket_id>`

**Methods:** `GET`, `POST`

**Purpose:** Renders the ticket details page and allows users to update ticket information.

**Sample output:**

![Edit_Ticket](/SCRUM_Webapp_Project/assets/images/Edit_Ticket.png)

---

### `delete_ticket(ticket_id)`

**Route:** `/Ticket/Delete/<int:ticket_id>`

**Methods:** `POST`

**Purpose:** Deletes a ticket with the specified ID.

---

### `new_ticket()`

**Route:** `/Ticket/New_Ticket`

**Methods:** `GET`, `POST`

**Purpose:** Renders the form for creating a new ticket and handles ticket creation.

**Sample output:**

![Create_Ticket](/SCRUM_Webapp_Project/assets/images/Create_Ticket.png)

---

### `sprint_planning(selected_sprint)`

**Route:** `/Sprint_Planning/<selected_sprint>`

**Methods:** `GET`

**Purpose:** Renders the sprint planning page, displaying tickets categorized into different stages for a specific sprint.

**Sample output:**

![Sprint_View](/SCRUM_Webapp_Project/assets/images/Sprint_View.png)

---

### `logout()`

**Route:** `/Logout`

**Methods:** `GET`

**Purpose:** Logs out the current user.

**Sample output:**

![Login_Screen](/SCRUM_Webapp_Project/assets/images/Login_Screen.png)
