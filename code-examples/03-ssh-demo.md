# SSH Setup for GitHub - Cross-Platform Guide

This guide works for macOS, Windows (PowerShell), and Windows Subsystem for Linux (WSL).

## Why SSH?

Since August 2021, GitHub no longer accepts passwords for Git operations. You have two options:
- **Personal Access Tokens (PAT)** - tokens you manually create and enter as passwords
- **SSH Keys** - cryptographic keys that authenticate automatically (recommended)

SSH is preferred because it's more secure and convenient once set up.

## Step 1: Check for Existing SSH Keys

**All Platforms (macOS, Windows PowerShell, WSL):**
```bash
ls -la ~/.ssh
```

If you see files like `id_ed25519` and `id_ed25519.pub`, you already have SSH keys. Skip to Step 4.

## Step 2: Generate SSH Keys

**All Platforms:**
```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```

**What this does:**
- `-t ed25519` creates a modern, secure key type
- `-C` adds your email as a comment

**When prompted:**
1. **File location**: Press Enter to use the default (`~/.ssh/id_ed25519`)
   - **macOS/WSL**: `~` = `/Users/yourusername/.ssh/` or `/home/yourusername/.ssh/`
   - **Windows PowerShell**: `~` = `C:\Users\yourusername\.ssh\`
2. **Passphrase**: Press Enter for no passphrase, or add one for extra security

## Step 3: Start SSH Agent and Add Key

### macOS and WSL:
```bash
# Start the SSH agent
eval "$(ssh-agent -s)"

# Add your key to the agent
ssh-add ~/.ssh/id_ed25519
```

### Windows PowerShell:
```powershell
# Start the SSH agent service
Get-Service ssh-agent | Set-Service -StartupType Manual
Start-Service ssh-agent

# Add your key to the agent
ssh-add $env:USERPROFILE\.ssh\id_ed25519
```

## Step 4: Copy Your Public Key

### macOS:
```bash
pbcopy < ~/.ssh/id_ed25519.pub
```

### WSL/Linux:
```bash
cat ~/.ssh/id_ed25519.pub
# Copy the output manually
```

### Windows PowerShell:
```powershell
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub | Set-Clipboard
```

**Alternative for all platforms:**
```bash
cat ~/.ssh/id_ed25519.pub
```
Then manually copy the output (starts with `ssh-ed25519`).

## Step 5: Add Key to GitHub

1. Go to [GitHub.com](https://github.com) and sign in
2. Click your profile picture → **Settings**
3. In the left sidebar, click **SSH and GPG keys**
4. Click **New SSH key**
5. Give it a title (like "My Laptop" or "Work Computer")
6. Paste your public key in the "Key" field
7. Click **Add SSH key**

## Step 6: Test Your Connection

**All Platforms:**
```bash
ssh -T git@github.com
```

**Expected output:**
```
Hi yourusername! You've successfully authenticated, but GitHub does not provide shell access.
```

If you see a warning about host authenticity, type `yes` and press Enter.

## Step 7: Use SSH URLs

When cloning repositories, use the SSH URL instead of HTTPS:

```bash
# SSH URL (use this)
git clone git@github.com:username/repository.git

# HTTPS URL (avoid this)
git clone https://github.com/username/repository.git
```

## Troubleshooting

### "Permission denied (publickey)"
- Make sure you copied the **public** key (`.pub` file) to GitHub
- Verify the SSH agent is running: `ssh-add -l`
- Re-add your key: `ssh-add ~/.ssh/id_ed25519` (or `ssh-add $env:USERPROFILE\.ssh\id_ed25519` on Windows PowerShell)

### "Could not open a connection to your authentication agent" (Windows)
- Run PowerShell as Administrator
- Restart the SSH agent service:
  ```powershell
  Stop-Service ssh-agent
  Start-Service ssh-agent
  ```

### Key not found
- Make sure you're in the right directory: `cd ~`
- Check the exact filename: `ls ~/.ssh/` (or `ls $env:USERPROFILE\.ssh` on Windows PowerShell)
- Use the correct path in `ssh-add`

## Platform-Specific Notes

### macOS
- SSH agent typically starts automatically
- Keys are stored in the system keychain

### Windows PowerShell
- SSH agent is available in Windows 10/11 by default
- May need to run as Administrator for service commands

### WSL (Windows Subsystem for Linux)
- Works exactly like Linux
- Keys are separate from Windows PowerShell keys
- SSH agent needs to be started each session (unless configured otherwise)

## Security Best Practices

1. **Use a passphrase** for your SSH key if you're on a shared computer
2. **Don't share your private key** (`id_ed25519` without `.pub`)
3. **Use different keys** for different services if needed
4. **Regularly rotate keys** (yearly is reasonable)
5. **Remove old keys** from GitHub when you no longer use them

---

**That's it!** Once set up, you'll never need to enter passwords for GitHub operations again.