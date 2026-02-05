# Project Vault 🔐

A secure, encrypted personal file storage system built with Python. Project Vault provides a safe and intuitive way to store, manage, and protect your sensitive files with enterprise-grade encryption.

## 🌟 Features

- **End-to-End Encryption**: Your files are encrypted using robust cryptographic algorithms before storage
- **User Authentication**: Secure login system to protect unauthorized access to your vault
- **Intuitive GUI**: User-friendly graphical interface built for ease of use
- **Organized Storage**: Structured vault system for managing your encrypted files
- **Activity Logging**: Comprehensive logging system to track vault activities
- **Database Management**: Efficient SQLite-based database for storing metadata and user information

## 📁 Project Structure

```
Project_voult/
├── auth/               # User authentication and authorization modules
├── crypto/             # Encryption and decryption utilities
├── database/           # Database management and operations
├── gui/                # Graphical user interface components
├── logs/               # Activity and error logging
├── utils/              # Helper functions and utilities
├── vault/              # Core vault storage functionality
├── main.py             # Application entry point
└── requirements.txt    # Python dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/naitikoss/Project_voult.git
cd Project_voult
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

## 🔧 Core Components

### Authentication System (`auth/`)
Handles user registration, login, and session management to ensure only authorized users can access the vault.

### Cryptography Module (`crypto/`)
Implements encryption and decryption algorithms to secure your files. Uses industry-standard cryptographic practices to ensure data confidentiality.

### Database Layer (`database/`)
Manages all data persistence including user credentials, file metadata, and vault configurations using SQLite.

### User Interface (`gui/`)
Provides an intuitive graphical interface for interacting with the vault, making file management simple and accessible.

### Vault Storage (`vault/`)
Core functionality for storing, retrieving, and managing encrypted files within the secure vault structure.

### Utilities (`utils/`)
Contains helper functions and common utilities used across the application for various operations.

### Logging System (`logs/`)
Tracks all vault activities, errors, and system events for audit trails and debugging purposes.

## 🛡️ Security Features

- **Strong Encryption**: Files are encrypted before being stored to disk
- **Secure Authentication**: Password-based authentication system
- **Activity Monitoring**: All vault operations are logged for security auditing
- **Data Integrity**: Ensures your files remain uncorrupted and tamper-proof

## 📝 Usage

1. **First Time Setup**
   - Launch the application
   - Create a new account with a strong password
   - Your master password will be used to encrypt/decrypt your files

2. **Adding Files**
   - Log in to your vault
   - Select files to add
   - Files are automatically encrypted and stored securely

3. **Retrieving Files**
   - Browse your vault through the GUI
   - Select files to decrypt and retrieve
   - Files are decrypted on-the-fly when accessed

4. **Managing Your Vault**
   - Organize files within your vault
   - View activity logs
   - Manage your account settings

## ⚠️ Important Notes

- **Never forget your master password**: Without it, your encrypted files cannot be recovered
- **Keep backups**: While your files are encrypted, consider backing up the vault directory
- **Secure your system**: Ensure your computer is free from malware to maintain vault security

## 🤝 Contributing

Contributions are welcome! If you'd like to improve Project Vault:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📋 Roadmap

- [ ] Multi-user support
- [ ] Cloud backup integration
- [ ] File sharing with encryption
- [ ] Mobile application
- [ ] Two-factor authentication
- [ ] File versioning system

## 🐛 Known Issues

Please check the [Issues](https://github.com/naitikoss/Project_voult/issues) page for current known issues and to report new ones.

## 📄 License

This project is available for personal and educational use. Please check the repository for specific license details.

## 👤 Author

**Naitik**
- GitHub: [@naitikoss](https://github.com/naitikoss)

## 🙏 Acknowledgments

- Thanks to all contributors who help improve this project
- Built with Python and love for privacy and security

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the documentation
- Review existing issues for solutions

---

**Note**: This is a personal file storage system. Always ensure you have backups of important files and never share your master password with anyone.

⭐ If you find this project useful, please consider giving it a star on GitHub!
