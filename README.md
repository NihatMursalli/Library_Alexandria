# Customer Requirements Document (CRD) for Library Management System

## 1. Introduction
The Library Management System (LMS) is designed to facilitate the management of books, users, and borrowing history within a library. This system provides functionalities for both administrators and users, ensuring efficient book tracking, borrowing, and return processes.

## 2. Objectives
- Provide a digital platform for managing library books and users.
- Enable book borrowing and returning with deadlines and overdue fines.
- Offer role-based access for administrators and users.
- Ensure data is stored securely in a structured format (JSON or CSV).

## 3. User Roles & Responsibilities

### 3.1 Administrator
- Add, update, and delete book records.
- View all books and their availability status.
- Track borrowed books and overdue returns.
- Manage system data and configurations.

### 3.2 Library User
- View the list of available books.
- Borrow books with a due date for return.
- Return borrowed books.
- Pay fines for overdue returns.

## 4. System Features

### 4.1 Book Management
- Each book has a unique ID, title, author, genre, price, and availability status.
- Books can be added, updated, or removed by administrators.

### 4.2 Borrowing System
- Users can borrow books for a maximum of 14 days.
- Borrowed books have a due date recorded in the system.
- Users cannot borrow a book that is currently unavailable.
- If a book is returned late, a fine of $1 per extra day is applied.

### 4.3 Admin Controls
- Admins can view all books, including borrowed ones.
- Admins can check overdue books and outstanding fines.
- System ensures that data integrity is maintained.

### 4.4 Data Storage & Security
- Data is stored in a structured JSON or CSV format.
- The admin panel requires authentication with hardcoded credentials.
- Input validation prevents errors such as borrowing unavailable books.

## 5. Implementation Details
- The system is a command-line interface (CLI) application.
- Developed using Python with object-oriented programming principles.
- Authentication is required for admin access.
- All data is managed through files rather than a database for simplicity.

## 6. Assumptions & Constraints
- Only a single admin account exists.
- No multi-user concurrency; actions are sequential.
- Fine amounts and borrowing duration are fixed.
- No graphical interface; all interactions occur through CLI.

## 7. Conclusion
This Library Management System provides an effective solution for handling book records, borrowing, and returns. It ensures ease of access for users while giving administrators the tools needed for efficient library management. Future improvements could include a database-backed system, enhanced user authentication, and a graphical user interface.
