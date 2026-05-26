# 📂 Dynamic File Organizer

A lightweight, fully customizable desktop tool that instantly declutters your Downloads folder. Built with Python, this app automatically sorts your files into specific folders (Photos, Videos, Documents, etc.) based on their file extensions. 

The best part? You don't need to know Python to customize it. The app reads its sorting rules directly from a simple JSON file, making it easy for anyone to add or modify categories on the fly.

## ✨ Features

* **⚙️ Dynamic Configuration:** Reads file extensions from an external `config.json` file. Add new file types without touching a single line of code!
* **🛡️ Collision Proof:** If a file with the same name already exists in the destination folder, it automatically renames the new file (e.g., `invoice_1.pdf`) instead of overwriting your data.
* **🚧 Safety Nets:** Safely skips over files that are currently open or in use by Windows without crashing the application.
* **📦 Standalone Executable:** Compiled into a single `.exe` file so non-developers can run it instantly without installing Python.

---

## 🚀 How to Use (For Regular Users)

You do not need to install Python to use this tool! 

1. Download both `app.exe` and `config.json` from the latest release.
2. Place both files in the same directory (e.g., your Desktop).
3. Double-click `app.exe`.
4. Watch your Downloads folder instantly organize itself!

### 📝 Customizing Your Folders
Want to add a new folder or file type? Just open `config.json` in Notepad or any text editor. 

```json
{
    "Photos": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Documents": [".pdf", ".docx", ".txt"]
}