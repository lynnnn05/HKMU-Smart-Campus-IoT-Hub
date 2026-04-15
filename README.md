# Course Project: COMP2090SEF / 8090SEF - Data Structures, Algorithms and Problem Solving 

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-brightgreen)
![Architecture](https://img.shields.io/badge/Architecture-OOP%20%7C%20SOLID-orange)
![Algorithm](https://img.shields.io/badge/Algorithm-Multi--Tier_Priority_%7C_Dijkstra-red)
 

An integrated software solution designed to modernize public healthcare logistics. This repository contains two distinct modules: an OOP-based hospital triage system (**Task 1**) and a graph-based optimal route navigator for ambulance dispatching (**Task 2**).


---
## 📑 Table of Contents
* [📂 Repository Structure](#repository-structure)
* [🚀 Task 1: Smart Hospital Triage & Queue Scheduling Engine](#task-1-smart-hospital-triage--queue-scheduling-engine)
* [🚑 Task 2: Smart Ambulance Navigator](#task-2-smart-ambulance-navigator-self-study-algorithm)
* [🎬 Task 2:Introduction Video](#task-2-introduction-video)
* [💻 Quick Start & User Guide](#quick-start--user-guide)
* [📜 Academic Declaration](#academic-declaration)
---

## 👥 Team Members

| Name | Student ID |
| :--- | :--- |
| **LIN Zhihong** | `[13771888]` |
| **LIN Yuhao** | `[Member 2 ID]` |
| **CHEN Yijun** | `[Member 3 ID]` |

---
<a id="repository-structure"></a>
## 📂 Repository Structure

```text
📦 COMP 2090SEF Project
 ┣ 📂 Task1/              
 ┃ ┣ 📜 main.py           
 ┃ ┣ 📜 interfaces.py        
 ┃ ┣ 📜 doctor.py 
 ┃ ┣ 📜 patient.py 
 ┃ ┣ 📜 server.py 
 ┃ ┗ 📜 ui.py        
 ┣ 📂 Task2/              
 ┃ ┣ 📜 navigator_logic.py
 ┃ ┗ 📜 app_gui.py
 ┃ ┗ 📷 output.png
 ┗ 📷 demo_cover.png
 ┗ 📜 README.md           
```

---
<a id="task-1-smart-hospital-triage--queue-scheduling-engine"></a>
## Task1: 🏥 Smart Hospital: Triage & Queue Scheduling Engine

An OOP-driven hospital triage simulation and queue management terminal. It demonstrates advanced software design patterns by implementing a **multi-dimensional, dynamic priority scheduling algorithm**, robust polymorphic service definitions, and a real-time fault-tolerant event loop.

### 🏛️ Deep Dive: The OOP Architecture
This system is a practical implementation of the four pillars of Object-Oriented Programming (OOP), ensuring the codebase is modular, scalable, and maintainable.

* **1. Abstraction (The Design Contract):** The system utilizes an Abstract Base Class (`MedicalService` in `interfaces.py`) to define the essential "contract". Using the `@abstractmethod` decorator, it mandates that any inheriting class must implement `get_fee()` and `process_patient()`.
* **2. Inheritance (Hierarchical Specialization):** Code reusability is maximized through a class hierarchy. `ExpertDoctor` and `EmergencyDoctor` inherit from the `Doctor` base class, sharing common `enqueue()` logic but specializing in department-specific roles.
* **3. Polymorphism (Dynamic Method Dispatch):** Demonstrates Method Overriding. `Doctor.get_fee()` returns 50.0, `ExpertDoctor.get_fee()` returns 150.0, and `EmergencyDoctor.get_fee()` returns 200.0. The correct fee is automatically determined at runtime.
* **4. Encapsulation (Information Hiding):** Sensitive data like a patient's financial balance is stored as a private attribute `self.__balance`. External modules must use the `deduct_fee()` method, which performs a safety check before allowing a transaction.

### 🧠 Algorithmic Logic: Multi-Dimensional Triage
The triage engine uses a sophisticated **Tuple-Comparison Priority Algorithm**. It calculates a priority tuple `(category, sequence)` to determine a patient's rank, ensuring FIFO stability within tiers.

| Priority Tier | Description | Condition Trigger | Rationale |
| :--- | :--- | :--- | :--- |
| **Tier 0** | 🚨 Emergency | `is_emergency = True` | Highest priority for life-saving care. |
| **Tier 1** | 👴 Elderly (Online) | `age >= 65` & `Online` | Seniority combined with a prior appointment. |
| **Tier 2** | 👴 Elderly (Walk-in)| `age >= 65` & `Walk-in`| Seniority, slightly penalized for no booking. |
| **Tier 3** | 📱 Standard (Online) | `< 65` & `Online` | Contractual appointment priority. |
| **Tier 4** | 🚶 Standard (Walk-in)| `< 65` & `Walk-in`| Standard sequential processing. |
| **Tier 5** | ⚠️ Missed Turn | `is_late = True` | Punitive downgrade for no-shows. |

### ⚙️ Operational Flow: The "No-Show" Mechanism
To mirror real-world hospital challenges, the system includes a stochastic event handler:
1. When "Call Next Patient" is triggered, there is a **20% chance** the patient is marked as a no-show.
2. If a no-show occurs, `mark_late()` is called, flag is set to `True`, and `seq` updates to the latest global tick.
3. Upon re-enqueuing, the algorithm automatically pushes them to the absolute end (Tier 5).

![Task 1 Demo](task1/Task1 GUI.png)

### 📂 Task1 Structure

* `interfaces.py`: Defines the **Abstract Data Type (ADT)** contract.
* `doctor.py`: Implements **Inheritance** and **Polymorphism** for medical staff.
* `patient.py`: Manages **Encapsulation** and the core **Priority Algorithm**.
* `server.py`: The **Backend Registry** managing doctor objects and global stats.
* `ui.py`: The **View Layer** handling the Tkinter GUI and event orchestration.
* `main.py`: The **Bootloader** that initializes the system.

---

<a id="task-2-smart-ambulance-navigator-self-study-algorithm"></a>
## 🚑 Task 2: Smart Ambulance Navigator (Self-Study)

**Objective:** To self-study and implement an advanced Data Structure and Algorithm (strictly beyond the lecture syllabus) to solve a real-world routing problem.

<a id="task-2-introduction-video"></a>
### 🎬 Introduction Video (Click the image below to watch the introduction video)
Welcome to the **HK Smart Ambulance Navigator**. Click the image below to watch our 5-minute project demonstration and algorithm walkthrough:

<div align="center">
  <a href="https://youtu.be/5L2XIRg7pQA" target="_blank">
    <img src="./demo_cover.png" alt="Demo Video Cover" width="800">
  </a>
</div>


### 📌 Problem Definition
When dispatching ambulances to hospitals, standard linear data structures cannot model a complex, congested city grid. This task builds a dynamic routing engine capable of navigating around traffic bottlenecks.

### 🧠 Self-Study Implementation
* **Data Structure: Weighted Graph (Adjacency List)**
  Modeled the city map using a Graph dictionary. This handles non-linear intersections and loops, keeping space complexity highly efficient at **O(V + E)**.
* **Algorithm: Dijkstra's Shortest Path**
  Utilized a Greedy Strategy combined with **Edge Relaxation**. The algorithm continuously evaluates neighboring nodes to find the global optimum, successfully avoiding pre-set "congestion traps" (e.g., a direct but 40-minute jammed road).

### ⏱️ Complexity Analysis

| Metric | Current Implementation | Optimal Implementation (Future Work) |
| :--- | :--- | :--- |
| **Search Mechanism** | Standard List Traversal | Min-Priority Queue (Heap) |
| **Time Complexity** | **O(V²)** | **O(E log V)** |
| **Space Complexity** | **O(V + E)** | **O(V + E)** |

<div align="center">
  <img src="./task2/output.png" alt="Task 2 Demo" width="800">
</div>

---
<a id="quick-start--user-guide"></a>
## 💻 Quick Start & User Guide

**1. Prerequisites**
* Python 3.x
* `Tkinter` (Standard Python GUI library, usually pre-installed)
* VScode or other python compilers

**2. Launch Task 1 (Hospital Triage System)**
```bash
python main.py
```
*(Usage: Register patients using the UI and observe the multi-tier priority sorting and stochastic no-show events in the event log.)*

**3. Launch Task 2 (Ambulance Navigator)**
```bash
python app_gui.py
```
*(Usage: Click the dispatch button to visualize Dijkstra's algorithm actively routing the ambulance around high-weight traffic traps to find the global optimum.)*

---
<a id="academic-declaration"></a>
## 📜 Academic Declaration
We declare that this project is our original work and has been developed strictly for academic assessment purposes for the COMP2090SEF course.
