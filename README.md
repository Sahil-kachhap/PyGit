# PyGit - A Simple Git Implementation in Python
---

## 📖 What is PyGit?

PyGit is a **Python implementation of Git** that demonstrates the core concepts and internals of version control systems.

## Core Components
### 1. **GitObject Class**

- Base class for all Git objects (Blob, Tree, Commit)
- Handles serialization/deserialization with zlib compression
- Generates SHA-1 hashes for object identification (real Git uses SHA-256 nowadays)

### 2. **Blob Objects**

- Store actual file contents
- Represent individual files in the repository

### 3. **Tree Objects**

- Represent directory structures
- Store references to blobs and other trees
- Maintain file permissions and names

### 4. **Commit Objects**

- Store metadata about commits (author, timestamp, message)
- Reference tree objects and parent commits
- Form the commit history chain

### 5. **Repository Class**

- Manages the `.git` directory structure
- Handles object storage and retrieval
- Implements Git commands (init, add, commit, checkout, etc.)

---

## Features

- **Repository Initialization** - Create new Git repositories
- **File Staging** - Add files to the staging area
- **Commit Creation** - Create commits with messages and metadata
- **Branch Management** - Create, switch, and delete branches
- **Commit History** - View commit logs and history
- **Status Checking** - Monitor repository state
- **Object Storage** - Efficient storage using SHA-1 hashing and compression

---

## 📦 Installation & Setup

### Prerequisites

- Python 3.7+
- No external dependencies required (uses standard libraries only)

### Quick Start

```bash
# Clone the repository
git clone <this-repo-url>
cd git_clone

# Run PyGit commands
python3 main.py init
python3 main.py add README.md
python3 main.py commit -m "Initial commit"
```

---

## 💻 Usage Examples

### Initialize a Repository

```bash
python3 main.py init
# Output: Initialized empty Git repository in ./.git
```

### Add Files to Staging

```bash
# Add single file
python3 main.py add main.py

# Add entire directory
python3 main.py add src/

# Add multiple files
python3 main.py add file1.py file2.py src/
```

### Create Commits

```bash
python3 main.py commit -m "Add new feature"
python3 main.py commit -m "Fix bug" --author "Sahil Kachhap <sahil@gmail.com>"
```

### Branch Operations

```bash
# List branches
python3 main.py branch

# Create new branch
python3 main.py checkout -b feature-branch

# Switch to existing branch
python3 main.py checkout main

# Delete branch
python3 main.py branch feature-branch -d
```

### View Repository Status

```bash
# Check working directory status
python3 main.py status

# View commit history
python3 main.py log -n 5
```

---

## 🗂️ Project Structure

```
git_clone/
├── main.py          # Main PyGit implementation
├── README.md        # This file
└── .git/           # Git repository (created after init)
    ├── objects/    # Git objects database
    ├── refs/       # References and branches
    ├── HEAD        # Current branch pointer
    └── index       # Staging area
```

---

## 🔍 How It Works

### 1. **Object Storage**

- Files are stored as **Blob objects** with compressed content
- Directories are represented as **Tree objects** with file references
- Each object gets a unique SHA-1 hash

### 2. **Staging Process**

- Files are read and converted to Blob objects
- Object hashes are stored in the index (staging area)
- Index tracks which files are ready for commit

### 3. **Commit Process**

- Creates a Tree object from the current index
- Generates a Commit object with metadata
- Updates branch reference to point to new commit

### 4. **Branch Management**

- Branches are just files pointing to commit hashes
- Checkout updates HEAD and restores working directory
- Branch creation copies current commit reference
