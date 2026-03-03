# 🏙️ Smart City IoT Sensor & Network Resource Manager

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![Status](https://img.shields.io/badge/Status-Preliminary_Submission-orange.svg)

> **Course:** COMP2090SEF Data Structures, Algorithms and Problem Solving
> **Note to Instructor/TA:** As approved, the implementation for both tasks is combined into a single integrated system. However, this documentation is clearly separated into Task 1 and Task 2 for grading purposes.

## 👥 Team Members
* **LIN Zhi Hong** (ID: 13771888)
* **[组员名字]** (ID: [组员学号])
* **[组员名字]** (ID: [组员学号])
*(Note: Detailed declaration of contribution will be attached in the final PDF reports.)*

## 📅 Project Timeline (Updates)
- [x] **2026.03.0x:** Completed integrated backend logic (`sensor_node.py`, `network_manager.py`).
- [x] **2026.03.08:** ✅ **Pre-submission** (GitHub Repository & Preliminary README).
- [ ] **2026.04.12:** 🔜 **Final Submission** (Task 1 & Task 2 PDF Reports, 5-min Intro Videos).

---

## 📖 Table of Contents
1. [📍 Task 1: OOP-based Application Development](#-task-1-oop-based-application-development)
2. [📍 Task 2: Self-study on Data Structure & Algorithm](#-task-2-self-study-on-data-structure--algorithm)
3. [💻 Preliminary Code Structure](#-preliminary-code-structure)
4. [⚙️ Installation & Quick Start](#️-installation--quick-start)
5. [👀 UI Gallery (Preview)](#-ui-gallery-preview)
6. [🎥 Introduction Videos](#-introduction-videos)

---

## 📍 Task 1: OOP-based Application Development
**Core Implementation:** `sensor_node.py`, `main.py`

### Description of Core Functions
This module simulates edge devices in a smart city network. It handles the initialization of different sensor types (Air Quality Monitors, Traffic Cameras) and manages their specific hardware states.

### Usage of OOP Concepts
* **Abstraction (ADT):** `AbstractSensor` enforces a standard `process_signal()` interface for all edge devices.
* **Encapsulation:** Hardware states (`_battery_level`) are protected and strictly accessed via getter/setter methods.
* **Inheritance & Polymorphism:** Specific classes (`AirQualitySensor`, `TrafficCamera`) inherit from `AbstractSensor` and override `process_signal()` for unique behaviors.
* **Class & Static Methods:** Uses a `@classmethod` to track the global active sensor registry and a `@staticmethod` for ADC conversion utility.
* **Magic Methods:** Overloads `__eq__` (preventing ID conflicts) and `__str__` (formatting output strings).

---

## 📍 Task 2: Self-study on Data Structure & Algorithm
**Core Implementation:** `network_manager.py`, `main.py`

### Introduction of Chosen Topics
* **New Data Structure:** **Graph (Adjacency List)**. The city's network topology is modeled as a weighted graph, which is highly memory-efficient for sparse embedded networks.
* **New Algorithm:** **Dijkstra's Shortest Path Algorithm**. Used to dynamically calculate the optimal, lowest-latency data transmission route between any two network nodes.

### Implementation Details
The `NetworkManager` class utilizes a Priority Queue (`heapq`) to execute Dijkstra's algorithm. It efficiently returns the best transmission path and total network latency for data packets traveling from remote sensors to central servers.

---

## 💻 Preliminary Code Structure
```text
📦 Smart-City-Resource-Manager
 ┣ 📜 main.py             # Top-level environment and Tkinter GUI
 ┣ 📜 network_manager.py  # Graph data structure & Dijkstra's algorithm
 ┣ 📜 sensor_node.py      # OOP modeling, ADTs, and sensor logic

 ┗ 📜 README.md           # Documentation
