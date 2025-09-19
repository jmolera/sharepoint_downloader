# sharepoint-downloader

A Python utility that automatically downloads and configures rclone to sync files from SharePoint/OneDrive sites.

## Features

- **Zero setup required** - Automatically downloads rclone binary
- **Interactive configuration** - Guided setup for SharePoint authentication
- **Real-time progress** - Live sync status and progress tracking
- **Cross-platform ready** - Windows focused, easily adaptable

## Requirements

- Python 3.6+
- Internet connection
- Windows (for current rclone binary)

## Quick Start

```bash
python sharepoint_downloader.py
```

The script will:
1. Download rclone.exe if not present
2. Open configuration wizard (first run only)
3. Prompt for sync parameters
4. Execute file synchronization

## Configuration

On first run, configure rclone with:
- **Remote type**: Microsoft OneDrive
- **Authentication**: Follow OAuth flow
- **Site access**: SharePoint site permissions

## Usage Example

```
Remote name: m30
Remote path: sites/ATMC30/Documentos compartidos/LOTE 1
Local destination: ./downloads
```

## Files Created

- `rclone.exe` - rclone binary (auto-downloaded)
- `%APPDATA%/rclone/rclone.conf` - Configuration file

## Troubleshooting

**"didn't find section in config file"** - Run rclone configuration first  
**"CRITICAL: Failed to create file system"** - Check remote name and authentication  
**Download fails** - Verify internet connection and firewall settings

## License

This project is provided as-is for educational and productivity purposes.