# NoSQL
This repo is for practicing interactions with MongoDB and other NoSQL databases.

## What is NoSQL?

NoSQL, or "Not Only SQL," refers to a category of databases that diverge from the traditional relational database management systems (RDBMS). These databases are designed to handle large volumes of unstructured, semi-structured, or structured data. NoSQL databases are often used in Big Data and real-time web applications.

## Difference between SQL and NoSQL

SQL databases are relational, using tables with predefined schemas for storing data. NoSQL databases are non-relational and offer greater flexibility, scalability, and performance. They can handle diverse data types and structures more efficiently.

## ACID

ACID stands for Atomicity, Consistency, Isolation, and Durability. It is a set of properties that guarantee database transactions are processed reliably. While most NoSQL databases sacrifice strict ACID compliance for scalability and performance, some provide ACID-like guarantees.

## Document Storage

Document storage is a NoSQL data model where data is stored in flexible, JSON-like documents. Each document can have its own structure, and collections of documents can be organized without a predefined schema.

## NoSQL Types

NoSQL databases come in various types, including key-value stores, document databases, wide-column stores, and graph databases. Each type is optimized for specific use cases and data models.

## Benefits of NoSQL Databases

- Scalability: NoSQL databases can easily scale horizontally to handle growing datasets and user loads.
- Flexibility: They can handle diverse data types and evolving schemas.
- High performance: NoSQL databases often offer faster read/write speeds compared to traditional SQL databases.
- Fault tolerance: Many NoSQL databases are designed for distributed architectures, ensuring high availability and fault tolerance.

## Querying from a NoSQL Database

Querying in NoSQL databases varies depending on the database type. Typically, NoSQL databases provide APIs or query languages tailored to their data model, such as MongoDB's query language for document databases.

## Inserting/Updating/Deleting in NoSQL Databases

NoSQL databases typically offer APIs or query languages for inserting, updating, and deleting data. Operations are optimized for scalability and performance, often supporting bulk operations and distributed transactions.

## Using MongoDB

MongoDB is a popular document-oriented NoSQL database. To use MongoDB:
1. Install MongoDB on your system.
2. Start the MongoDB server.
3. Use the MongoDB shell or a programming language driver to interact with the database.
4. Create databases, collections, and documents as needed.
5. Query, insert, update, and delete data using MongoDB's query language and APIs.