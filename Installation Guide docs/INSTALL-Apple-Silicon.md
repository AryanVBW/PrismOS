# PrismOS Installation on Apple Silicon (M1/M2/M-series)

This guide walks you through installing PrismOS on Apple Silicon Macs (M1, M2, and later). It's written for beginners and focuses on minimizing data loss and enabling an easy rollback.

## What you'll find in this guide

- System requirements
- Step-by-step installation (preparation, flashing, booting, first-run)
- Screenshots (placeholders) and how to capture them
- Troubleshooting
- FAQ
- Video tutorial plan and recording script

---

## System requirements

Minimum:

- Mac with Apple Silicon (M1/M2/Pro/Max/Ultra or later). Older Intel Macs are not covered here.
- macOS 12 Monterey or later (recommended macOS Ventura or newer)
- 8 GB RAM (4 GB may work for some builds, but 8 GB is recommended)
- 30 GB free disk space for the installer and temporary files (50 GB recommended if you plan to allocate partitions)
- USB-C flash drive (16 GB+) for rescue media (optional but recommended)
- A second working Mac or external storage to keep backup of your data

Software prerequisites:

- Xcode command line tools (for some helper scripts):
  - Install: `xcode-select --install`
- Python 3.9+ (system Python may be present). The repository contains Python scripts used by the installer; having a Python 3 interpreter available is helpful.
- Homebrew is optional but convenient for installing dependencies.

Backups and safety:

- Back up your data (Time Machine or manual copy). Installing OS-level modifications can cause data loss.
- Have a macOS recovery volume or bootable macOS installer handy to restore the system if needed.

Permissions and security considerations:

- You may need to temporarily reduce security (recovery -> Startup Security Utility) to allow booting from external media. Understand the risks.
- The guide explains reversible steps where possible.

---

## Step-by-step installation guide

Note: This guide assumes you are comfortable running terminal commands. If not, follow the GUI instructions and ask for help before proceeding.

High-level steps:
1. Verify hardware & backup
2. Clone or download PrismOS repository
3. Prepare the installer and rescue media
4. Boot into Recovery to adjust security (if required)
5. Install PrismOS
6. Post-install verification and cleanup

### 1) Verify hardware & backup

- Check your Mac model and chip:
  - System Settings > About This Mac (GUI)
  - or run in Terminal: `sysctl -n machdep.cpu.brand_string || uname -m`
- Make a full backup. Use Time Machine or copy your home folder to an external drive.

![About This Mac](Installation Guide docs/images/01-about-this-mac.svg)
Placeholder screenshot: `Installation Guide docs/images/01-about-this-mac.svg`

### 2) Clone or download PrismOS

Open Terminal and run:

```bash
# clone the repository
git clone https://github.com/AryanVBW/PrismOS.git
cd PrismOS
```

If you already have the repo, `git pull` to update. Verify files like `install.sh`, `osinstall.py`, and `asahi_firmware/` exist.

![Clone Repo](Installation Guide docs/images/02-clone-repo.svg)
Placeholder screenshot: `Installation Guide docs/images/02-clone-repo.svg`

### 3) Prepare the installer and rescue media

- Install prerequisites (example):

```bash
# macOS: install Xcode CLT
xcode-select --install

# Optional: install brew, python, etc.
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python git
```

- Create a USB-C rescue stick (optional but recommended):

1. Insert a USB drive (16 GB+). Open Disk Utility and format as "Mac OS Extended (Journaled)" or `exFAT` if you prefer.
2. Use the included `install.sh` or `osinstall.py` scripts as directed in this repo.

Example (dry-run):

```bash
# Review the installer script before running
less install.sh

# Run installer in verbose/dry-run mode if available
./install.sh --dry-run
```

![Prepare USB](Installation Guide docs/images/03-prepare-usb.svg)
Placeholder screenshot: `Installation Guide docs/images/03-prepare-usb.svg`

### 4) Boot into Recovery to adjust security (if required)

Apple Silicon requires shutting down and booting into recovery by holding the power button. Follow Apple's official instructions:

- Shutdown your Mac
- Press and hold the power button until "Loading startup options" appears
- Click Options -> Continue -> Utilities -> Startup Security Utility
- If you need to allow external booting, set "External boot" to "Allow booting from external media" and reduce Secure Boot to "Medium Security" or similar

Important: Re-enable stricter security after installation if you lower it.

![Recovery Options](Installation Guide docs/images/04-recovery-options.svg)
Placeholder screenshot: `Installation Guide docs/images/04-recovery-options.svg`

### 5) Install PrismOS

This step depends on the installer script. The repo includes `install.sh` and `osinstall.py` which automate many steps. Use these with caution and read the scripts.

Example safe flow:

```bash
# run in the repo root
# show what will happen
./install.sh --check

# when ready, run interactively
sudo ./install.sh
```

What the script typically does (read the script to confirm):
- Verifies firmware blobs and collects asahi_firmware
- Prepares a new volume/partition or installs to a spare drive
- Copies files and configures boot entries

If the installer offers a "dry-run" or "--no-write" flag, prefer that first.

![Run Installer](Installation Guide docs/images/05-run-installer.svg)
Placeholder screenshot: `Installation Guide docs/images/05-run-installer.svg`

### 6) Post-install verification and cleanup

- Reboot the system and choose PrismOS (or the installed volume) from the boot picker (hold power until startup options appear).
- Verify the kernel and drivers load:

```bash
# check dmesg for errors
sudo dmesg | tail -n 200

# check loaded modules or prism-specific logs
# (replace with actual PrismOS logging commands)
journalctl -b | head -n 200
```

- Restore security settings in Recovery -> Startup Security Utility if you changed them.

![First Boot](Installation Guide docs/images/06-first-boot.svg)
Placeholder screenshot: `Installation Guide docs/images/06-first-boot.svg`

---

## Screenshots and how to contribute them

We included placeholders in `docs/images/`. To add your screenshots:
Mock screenshots have been added in the respective places

1. Capture a screenshot on macOS with:
   - Entire screen: Cmd+Shift+3
   - Selection: Cmd+Shift+4
2. Rename files using the step prefix and preferred format (SVG or PNG). Example filenames:
   - `01-about-this-mac.svg` or `01-about-this-mac.png`
   - `02-clone-repo.svg` or `02-clone-repo.png`
3. Place files in `docs/images/` and update this markdown only if you change filenames.
4. Open a PR with the images and the updated markdown. Keep images under 1.5 MB when possible.

Notes:
- SVGs are preferred for placeholder images (they scale cleanly). For terminal screenshots, PNG is usually better because it preserves pixel-perfect rendering.
- When capturing terminal output, increase font size and window width so text is readable in thumbnails.

Converting SVG to PNG (optional, local)

If you'd like PNGs for maximum compatibility on all viewers, convert locally using one of these commands on your Mac or Linux machine:

```bash
# Using rsvg-convert (recommended)
rsvg-convert -w 1280 -h 720 -o 01-about-this-mac.png 01-about-this-mac.svg

# Using ImageMagick
magick convert -background none -resize 1280x720 01-about-this-mac.svg 01-about-this-mac.png
```

Note: This dev environment does not include SVG->PNG conversion tools, so I did not generate PNGs here. If you run the commands above locally and push PNGs to `Installation Guide docs/images/`, I can update the docs in a follow-up PR.

---

## Troubleshooting

Common problems and fixes:

1) Installer aborts with permission errors
   - Ensure scripts are executable and run with `sudo` if required.
   - Check file permissions: `ls -l install.sh` and set `chmod +x install.sh`.

2) Mac won't boot external media after installation
   - Verify Startup Security Utility settings in Recovery.
   - Recreate rescue USB and try booting from it.

3) Missing drivers or devices (Wi-Fi, Bluetooth, trackpad)
   - Check `dmesg` or `journalctl` for driver errors
   - Ensure `asahi_firmware/` has correct blobs. Re-run `./install.sh --fetch-firmware` if present.

4) Kernel panics or hangs on boot
   - Boot into recovery and restore from backup.
   - Try safe boot or verbose boot to capture logs: hold power and run options.

Logs to gather when asking for help:
- `sudo dmesg > /tmp/dmesg.txt`
- `journalctl -b > /tmp/journal.txt`
- `system_profiler SPHardwareDataType > /tmp/hardware.txt`

Attach these logs to your issue when filing a bug.

---

## FAQ

Q: Is PrismOS compatible with my Mac?
A: PrismOS targets Apple Silicon Macs. Compatibility depends on specific hardware revisions and drivers. Check issues and the `asahi_firmware/` directory for supported devices.

Q: Can I dual-boot macOS and PrismOS?
A: Yes, the installer supports installing to a separate volume or drive. Back up macOS and ensure you choose the correct target during installation.

Q: How do I roll back to macOS only?
A: Restore from your Time Machine backup or reinstall macOS using a bootable installer.

Q: Where can I get help?
A: Open an issue in this repository with the logs listed in the Troubleshooting section.

---

## Video tutorial plan (how to create and what to include)

We can't include a video in this repo, but here's a script and checklist for recording a short 5–10 minute tutorial. Contributors can record and upload to YouTube or GitHub Releases.

Suggested structure:
- Intro (10–20s): What is PrismOS and what the video shows
- Prereqs & backup (30–45s): Explain requirements and backup step
- Prepare repo & rescue media (1–2 mins): Show cloning, formatting USB
- Recovery & security (45–60s): Show entering recovery and security setting
- Installing (1–2 mins): Run installer with highlights; explain prompts
- First boot & verification (45–60s): First boot and show logs
- Troubleshooting tip (30s): Quick fix for a common problem
- Outro/links (10–20s): Link to repo and docs

Recording checklist:
- Resolution: 1920x1080
- Format: MP4 (H.264)
- Tools: QuickTime Player (macOS), OBS (cross-platform)
- Microphone: use a clear mic and record short captions
- Include captions/subtitles for accessibility

Suggested filename: `prismos-install-apple-silicon.mp4`

Upload tips:
- Host on YouTube (unlisted or public) and link in README
- Or add a release asset to GitHub Releases

---

## Contributing improvements

- To add real screenshots, create a branch, add images to `docs/images/`, update this markdown to replace placeholders, and open a PR.
- For video submissions, link the video URL in the README and open a PR to add the link.

---

## Notes and acknowledgements

This guide was prepared for Hacktoberfest 2025 documentation contributions. If you find gaps or have corrections, please open an issue or PR.
