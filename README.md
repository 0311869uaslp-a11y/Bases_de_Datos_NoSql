# NoSQL Databases

Repository containing exercises, implementations, and practical work developed during my academic training in **NoSQL Databases** at the **Universidad Autónoma de San Luis Potosí (UASLP)**.

The coursework explores non-relational database technologies and their integration with software applications, with practical work involving **MongoDB, MongoDB Atlas, Redis, CRUD operations, JSON/document-based data modeling, and Python database integration**.

The repository provides practical experience with different approaches to data storage beyond traditional relational database systems.

---

## Course Overview

Traditional relational databases organize information primarily through tables, rows, columns, and relationships.

NoSQL databases provide alternative data models designed for different types of applications and data-access patterns.

```text
                    Databases
                        |
            +-----------+-----------+
            |                       |
            v                       v
       Relational                 NoSQL
            |                       |
            v                       v
       Tables / SQL          Flexible Data Models
                                    |
                        +-----------+-----------+
                        |                       |
                        v                       v
                  Document Data            Key-Value Data
                        |                       |
                        v                       v
                     MongoDB                  Redis
```

The coursework provides practical experience with both **document-oriented** and **key-value** database technologies.

---

# Topics Covered

The repository includes practical work related to:

- NoSQL database fundamentals
- Non-relational data models
- MongoDB
- MongoDB Atlas
- Redis
- Document-oriented databases
- Key-value databases
- JSON and document-based data modeling
- Database creation
- Collections
- Documents
- CRUD operations
- Queries
- Data insertion
- Data retrieval
- Data updates
- Data deletion
- Python integration
- Application-to-database communication

---

# Relational vs. NoSQL Databases

Relational and NoSQL databases represent information differently.

A relational database typically organizes information as:

```text
Database
   |
   v
Tables
   |
   v
Rows + Columns
   |
   v
Relationships
```

A document-oriented NoSQL database can instead organize information as:

```text
Database
   |
   v
Collections
   |
   v
Documents
   |
   v
Fields / Nested Data
```

This provides greater flexibility for applications where records do not necessarily share exactly the same structure.

---

# MongoDB

A major component of the coursework focuses on **MongoDB**, a document-oriented NoSQL database.

Instead of storing information in conventional relational tables, MongoDB organizes data into **collections and documents**.

```text
MongoDB
   |
   v
Database
   |
   v
Collection
   |
   v
Documents
   |
   v
Fields
```

A document can conceptually look like:

```json
{
  "name": "Example",
  "category": "Sensor",
  "value": 25.4,
  "active": true
}
```

This representation allows related information to be stored naturally using document structures.

---

# Document-Oriented Data Modeling

MongoDB stores information using document structures closely related to JSON.

For example:

```json
{
  "student": {
    "name": "Example Student",
    "courses": [
      "Data Science",
      "Artificial Intelligence",
      "NoSQL"
    ],
    "active": true
  }
}
```

Document-oriented modeling provides flexibility for:

- Nested information
- Arrays
- Variable document structures
- Application-oriented data
- Semi-structured information

The coursework provides experience understanding how information can be represented without relying exclusively on normalized relational tables.

---

# Collections and Documents

MongoDB uses **collections** to organize groups of documents.

```text
Database
   |
   +-- users
   |     |
   |     +-- Document 1
   |     +-- Document 2
   |     `-- Document 3
   |
   +-- products
   |     |
   |     +-- Document 1
   |     `-- Document 2
   |
   `-- measurements
         |
         +-- Document 1
         +-- Document 2
         `-- Document N
```

This structure differs from the table-based organization used by relational databases.

---

# CRUD Operations

The repository includes practical exercises involving the four fundamental database operations:

```text
C -> Create
R -> Read
U -> Update
D -> Delete
```

These operations form the basis of interaction between applications and databases.

---

## Create

New documents can be inserted into a collection.

Conceptually:

```javascript
db.collection.insertOne({
    name: "Example",
    value: 100
})
```

The objective is to understand how application data can be persisted inside a document-oriented database.

---

## Read

Documents can be retrieved using queries.

Conceptually:

```javascript
db.collection.find({
    value: 100
})
```

Queries allow applications to retrieve only the information that satisfies specific conditions.

---

## Update

Existing documents can be modified.

Conceptually:

```javascript
db.collection.updateOne(
    { name: "Example" },
    { $set: { value: 150 } }
)
```

This demonstrates how stored information can evolve without recreating an entire dataset.

---

## Delete

Documents can also be removed.

Conceptually:

```javascript
db.collection.deleteOne({
    name: "Example"
})
```

Together, these operations provide the fundamental interaction model required by most database-backed applications.

---

# MongoDB Atlas

The coursework also includes **MongoDB Atlas**, MongoDB's cloud database platform.

The general architecture can be represented as:

```text
Local Application
       |
       v
   Internet
       |
       v
MongoDB Atlas
       |
       v
Cloud Database
       |
       v
Collections / Documents
```

Working with MongoDB Atlas introduces the concept of using a database hosted outside the local development environment.

This provides experience with:

- Cloud-hosted databases
- Remote database connections
- Application/database separation
- Database connection configuration

---

# Python + MongoDB

The coursework includes integration between **Python applications and MongoDB**.

A typical architecture is:

```text
Python Application
        |
        v
 MongoDB Driver
        |
        v
    MongoDB
        |
        v
   Collection
        |
        v
    Documents
```

This demonstrates how a programming language can interact programmatically with a NoSQL database.

The application can perform operations such as:

```text
Python
   |
   +----> Insert Data
   |
   +----> Query Data
   |
   +----> Update Data
   |
   +----> Delete Data
   |
   `----> Process Results
```

This integration connects database concepts with software and data-processing workflows.

---

# Redis

The repository also contains practical work related to **Redis**.

Redis follows a different approach from MongoDB and is commonly associated with **key-value data storage**.

Conceptually:

```text
Key                 Value
--------------------------------
"user:1"        ->  user data
"sensor:25"     ->  measurement
"counter"       ->  150
"status"        ->  active
```

The fundamental structure can be represented as:

```text
Application
    |
    v
   Key
    |
    v
  Redis
    |
    v
  Value
```

This provides experience with a second NoSQL paradigm rather than focusing exclusively on document databases.

---

# MongoDB vs. Redis

The coursework provides exposure to two different approaches to NoSQL data management.

| MongoDB | Redis |
|---|---|
| Document-oriented | Key-value oriented |
| Collections | Keys |
| Documents | Values |
| JSON-like structures | Key-value structures |
| Flexible documents | Fast data access model |
| Persistent application data | Simple key-based data access |

The purpose of studying both technologies is to understand that **NoSQL is not a single database model**.

Different database architectures are suitable for different application requirements.

---

# JSON-Based Data

JSON-style representations are particularly important when working with document databases and modern applications.

Example:

```json
{
  "device_id": 15,
  "location": "laboratory",
  "measurements": {
    "temperature": 24.8,
    "humidity": 52.1
  },
  "active": true
}
```

Nested structures allow related information to be represented naturally.

```text
Document
   |
   +-- device_id
   |
   +-- location
   |
   +-- measurements
   |      |
   |      +-- temperature
   |      `-- humidity
   |
   `-- active
```

This type of structure is particularly useful when applications naturally generate semi-structured information.

---

# Application Integration

One of the most important aspects of the coursework is understanding that databases are normally components inside larger software systems.

```text
            User / Data Source
                    |
                    v
               Application
                    |
                    v
              Business Logic
                    |
                    v
              Database Layer
                    |
            +-------+-------+
            |               |
            v               v
         MongoDB           Redis
            |               |
            v               v
        Documents       Key-Values
```

The database therefore becomes part of an end-to-end application architecture rather than an isolated technology.

---

# Database Workflow

A typical workflow explored through the exercises can be represented as:

```text
Data
 |
 v
Application
 |
 v
Database Connection
 |
 v
Data Validation / Preparation
 |
 v
CRUD Operation
 |
 +----------------------------+
 |        |         |         |
 v        v         v         v
Create   Read     Update    Delete
 |        |         |         |
 +--------+---------+---------+
              |
              v
          Database
              |
              v
         Query Results
              |
              v
          Application
```

---

# NoSQL and Data Science

NoSQL databases can also be useful within Data Science and Machine Learning workflows.

```text
Data Sources
     |
     v
NoSQL Database
     |
     v
Data Extraction
     |
     v
Python
     |
     v
Data Processing
     |
     v
Analytics / ML
```

For example, semi-structured application or sensor information can be stored in a document database and later retrieved for analytical processing.

This makes database knowledge complementary to:

- Data preprocessing
- Data analysis
- Machine Learning
- IoT analytics
- Backend development
- Data pipelines

---

# Relationship with IoT

Document and NoSQL databases are also relevant to IoT applications, where devices can generate heterogeneous information.

```text
IoT Devices
     |
     v
Measurements
     |
     v
Backend / API
     |
     v
NoSQL Database
     |
     v
Data Processing
     |
     v
Dashboard / Analytics
```

Sensor records can naturally contain:

- Device identifiers
- Timestamps
- Measurements
- Location
- Device metadata
- Status information

This makes flexible data representations useful when integrating heterogeneous devices and applications.

---

# SQL and NoSQL

My broader project experience includes both relational and non-relational database technologies.

```text
                    Data Management
                          |
              +-----------+-----------+
              |                       |
              v                       v
             SQL                    NoSQL
              |                       |
              v                       v
         PostgreSQL             MongoDB / Redis
           MySQL
              |                       |
              v                       v
        Relational Data       Flexible Data Models
```

This provides experience selecting and working with different data-management approaches depending on the structure and requirements of the application.

---

# Skills Developed

Through the exercises in this repository, the course develops practical knowledge in:

- NoSQL databases
- MongoDB
- MongoDB Atlas
- Redis
- Document-oriented databases
- Key-value databases
- JSON/document data modeling
- Collections and documents
- CRUD operations
- Database queries
- Data insertion
- Data retrieval
- Data updates
- Data deletion
- Cloud-hosted databases
- Python/database integration
- Application/database communication
- Non-relational data management

---

# Technologies

Technologies represented in the coursework include:

```text
MongoDB
MongoDB Atlas
Redis
Python
JSON
```

These technologies complement my experience with relational database systems such as **PostgreSQL and MySQL** in other academic, research, and software projects.

---

# Relationship with Data Science Training

The NoSQL coursework complements the other areas of my Data Science and Artificial Intelligence training:

```text
               Data Science & AI
                       |
       +---------------+---------------+
       |               |               |
       v               v               v
 Data Management   Data Analysis   Machine Learning
       |
   +---+---+
   |       |
   v       v
  SQL     NoSQL
           |
       +---+---+
       |       |
       v       v
    MongoDB   Redis
```

Related areas of my training include:

- Artificial Intelligence
- Data Mining
- Machine Learning
- Deep Learning
- Graph Theory
- Data preprocessing
- Python programming

---

# Academic Context

This repository contains coursework developed at:

**Universidad Autónoma de San Luis Potosí (UASLP)**  
San Luis Potosí, Mexico

The work forms part of my academic training in **NoSQL Databases and Data Science**, complementing my experience in relational databases, Machine Learning, software development, and data analytics.

---

# Repository Purpose

The purpose of this repository is to preserve and document practical exercises involving non-relational database technologies.

The repository demonstrates a progression from understanding NoSQL concepts to integrating databases with applications:

```text
NoSQL Fundamentals
        |
        v
Data Models
        |
   +----+----+
   |         |
   v         v
Documents  Key-Value
   |         |
   v         v
MongoDB    Redis
   |
   v
MongoDB Atlas
   |
   v
CRUD Operations
   |
   v
Python Integration
   |
   v
Database-Backed Applications
```

Together, these exercises provide practical foundations in **non-relational data management and application/database integration**.

---

# Author

**José Luis Romero Vázquez**

Electronics Engineer and Data Scientist with international graduate education in Electronic Engineering, Telecommunications, and Computer Networks, with applied experience in Machine Learning, data analytics, IoT, databases, research, and software development.

**LinkedIn:**  
https://www.linkedin.com/in/jose-luis-romero-vazquez-486569209

**GitHub:**  
https://github.com/0311869uaslp-a11y
