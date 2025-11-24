# Project Statement: Simple Train Reservation System

---

## 1. Problem Statement

The manual management of train schedules, routes, and ticket bookings is prone to errors, inefficiency, and delays. There is a need for a simple, automated system that can reliably store train information and facilitate basic reservation and administrative tasks. The challenge is to create a functional, application that efficiently handles user authentication (Admin and Passenger) and provides core features like viewing train details, booking tickets, and managing the train inventory.

---

## 2. Scope of the Project

The scope of this project is limited to developing a application in Python.

The application will cover the following main areas:
* **User Authentication:** Implementing a login system for two distinct roles: **Admin** and **Passenger**.
* **Train Data Management:** Storing and retrieving pre-defined train information, including the train number, route, and schedule.
* **Passenger Operations:** Allowing passengers to view train details, book tickets (with basic route validation), and simulate ticket cancellation.
* **Administrative Operations:** Providing administrators with the ability to add new trains, remove existing trains, and view all system trains.

The project **does not** include:
* Integration with a persistent database (data is stored in memory using dictionaries).
* Real-time seat availability or complex fare calculations.
* A Graphical User Interface (GUI) or web interface.
* Payment processing.

---

## 3. Target Users

The system is designed for two primary target user groups:

| Target Group | Description | Primary Needs Addressed |
| :--- | :--- | :--- |
| **Passengers** | Individuals who need to quickly find train information, book tickets, and manage existing reservations. | Easy access to train schedules and simple, functional booking/cancellation processes. |
| **Administrators** | Personnel responsible for maintaining the system's data integrity, updating the list of available trains, and overseeing the system. | Tools to add, remove, and view the entire train inventory efficiently. |

---

## 4. High-Level Features

* **Secure Role-Based Login:** Separate login flows for Admin and Passenger users, including a sign-up option for new passengers.
* **Train Information Retrieval:** Ability to search for and display complete details (route, schedule, number) for any train by name.
* **Ticket Booking and Validation:** A function to book seats on a specific train with validation checks for the existence of the train, the validity of the start and end stations, and correct route sequencing.
* **Train Management:** Admin functionalities to add new trains (specifying routes and schedules) and remove trains from the system.
* **Cancellation Utility:** A dedicated utility for passengers to simulate the cancellation of a booked ticket.