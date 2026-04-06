# 🏢 HKMU Smart Campus - Edge IoT Energy Hub

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![OOP](https://img.shields.io/badge/paradigm-Object--Oriented-success.svg)
![Data Structure](https://img.shields.io/badge/Data_Structure-FIFO_Queue-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green)

> **Course Project:** COMP2090SEF Data Structures, Algorithms and Problem Solving  
> **Task 1:** OOP-based Application Development  

An enterprise-grade, Object-Oriented IoT energy management dashboard designed to solve real-world energy waste problems within the Hong Kong Metropolitan University (HKMU) campus. It simulates a localized Edge AI node that manages various campus devices, calculates dynamic power consumption, and executes asynchronous tasks via a FIFO Command Queue.

---


##Task 1:## OOP-based Application Development  
## 📑 Table of Contents
1. [Problem Definition & Motivation](#-1-problem-definition--motivation)
2. [Key Features](#-2-key-features)
3. [Object-Oriented Architecture (Rubric Mapping)](#-3-object-oriented-architecture-rubric-mapping)
4. [Repository Structure](#-4-repository-structure)
5. [Getting Started & Usage](#-5-getting-started--usage)
6. [Acknowledgments & Academic Declaration](#-6-acknowledgments--academic-declaration)

---

## 📌 1. Problem Definition & Motivation
**Real-World Context:** University campuses face significant challenges in managing energy efficiency. In places like HKMU's EECS laboratories (Block E) and lecture theaters (Block A), high-power devices such as Air Conditioners and specialized measurement tools (e.g., Oscilloscopes) are frequently left running idle. 

**The Solution:** This project builds a **Smart Campus IoT Edge Controller**. It provides a centralized software hub utilizing OOP principles to abstract, monitor, and intelligently schedule power states for different device types, demonstrating a scalable solution for a Green Campus (ESG) initiative.

---

## ✨ 2. Key Features
* **🔌 Polymorphic Analytics:** Dynamically calculates real-time power draw (W) and estimated hourly costs (HKD) using device-specific logic.
* **⏳ Asynchronous Task Queue (FIFO):** Incorporates core Data Structure concepts. Hardware commands are wrapped as lambda functions and queued for safe, sequential batch processing.
* **🍃 One-Click Eco-Mode:** A centralized aggregation command that forces all active devices into a powered-down state to prevent overnight energy waste.
* **🖥️ Modern Dark-Mode GUI:** A decoupled, responsive Tkinter dashboard demonstrating professional UI/UX separation from business logic.

![Dashboard Screenshot](docs/screenshot.png)

---

## 🏗️ 3. Object-Oriented Architecture (Rubric Mapping)
This project strictly adheres to all OOP concepts required by the COMP2090SEF curriculum.

### I. Abstraction & Inheritance
* **`CampusDevice (ABC)`**: An Abstract Base Class defining the blueprint for all hardware nodes.
* **Derived Classes**: `SmartAC` and `LabOscilloscope` inherit from the base class, implementing localized behaviors.

### II. Polymorphism
* The Hub calls `get_power_consumption()` on all objects without needing to know their specific type. Each class calculates its draw using its own unique algorithm (e.g., Temperature delta for AC vs. State-based for Lab tools).

### III. Encapsulation
* All sensitive attributes (e.g., `_device_id`, `_is_on`) are protected and only accessible via secure getters and setters, ensuring system integrity.

### IV. Advanced Features
* **Class/Static Methods:** Used for system-wide analytics and room code validation.
* **Magic Methods:** Overridden `__str__` for logging, `__eq__` for ID verification, and `__add__` for summing power consumption.

---

## 📂 4. Repository Structure
The project is organized into separate folders for Task 1 and Task 2 to meet the submission requirements.

```text
📦 HKMU-Smart-Campus-IoT-Hub
 ┣ 📂 Task1/              # OOP-based IoT Dashboard
 ┃ ┣ 📜 main.py           # Entry point
 ┃ ┣ 📜 devices.py        # OOP Data Models
 ┃ ┣ 📜 hub_controller.py # Logic & Command Queue
 ┃ ┗ 📜 gui_app.py        # Tkinter Presentation Layer
 ┣ 📂 Task2/              # Self-Study: Algorithm & Data Structure
 ┃ ┗ 📜 .gitkeep          # (Placeholder for Task 2 content)
 ┗ 📜 README.md           # Main Project Documentation
