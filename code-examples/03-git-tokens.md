# GitHub Personal Access Token - Quick Setup

If you prefer not to set up SSH keys, you can use Personal Access Tokens (PAT) for HTTPS authentication with GitHub.

## Why Use Personal Access Tokens?

Since August 2021, GitHub no longer accepts passwords for Git operations. Your options are:
- **SSH Keys** (recommended for professionals)
- **Personal Access Tokens** (easier setup, good for beginners)

## Step 1: Create Your Token

### Navigate to Token Settings
1. Go to [GitHub.com](https://github.com) and sign in
2. Click your **profile picture** (top right corner)
3. Click **Settings**
4. Scroll down to **Developer settings** (left sidebar)
5. Click **Personal access tokens**
6. Click **Tokens (classic)**

**Quick link:** https://github.com/settings/personal-access-tokens/new

### Generate New Token
1. Click **Generate new token (classic)**
2. Enter your GitHub password if prompted

### Configure Your Token
- **Note**: Give it a descriptive name (e.g., "Git Command Line Access")
- **Expiration**: Choose 30 days, 90 days, or custom (never use "No expiration" for security)
- **Scopes**: Check the **`repo`** box for full repository access

### Save Your Token
1. Click **Generate token**
2. **IMMEDIATELY COPY THE TOKEN** - you won't see it again!
3. Save it somewhere secure (password manager, secure note, etc.)

## Step 2: Use Your Token

### For Git Operations
When Git prompts for credentials:

```
Username: your-github-username
Password: ghp_your-personal-access-token-here
```

**Important:** Use the token as your password, not your actual GitHub password!

### Example: Clone a Repository
```bash
git clone https://github.com/username/repository.git
# When prompted:
# Username: username
# Password: ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Example: Push Changes
```bash
git push origin main
# When prompted:
# Username: username  
# Password: ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## Token Management

### Store Credentials (Optional)
To avoid entering the token every time:

**Windows:**
```bash
git config --global credential.helper manager-core
```

**macOS:**
```bash
git config --global credential.helper osxkeychain
```

**Linux:**
```bash
git config --global credential.helper store
```

After running this, Git will remember your token after the first use.

### Token Security Best Practices

1. **Treat tokens like passwords** - never share them
2. **Set expiration dates** - rotate tokens regularly
3. **Use minimal scopes** - only grant necessary permissions
4. **Store securely** - use a password manager
5. **Revoke unused tokens** - clean up old tokens regularly

### Regenerate Expired Tokens
1. Go back to GitHub Settings → Developer settings → Personal access tokens
2. Click on your expired token
3. Click **Regenerate token**
4. Update your stored credentials with the new token

## Troubleshooting

### "Authentication failed" Error
- Double-check you're using the token, not your GitHub password
- Verify the token hasn't expired
- Ensure the token has the correct scopes (check `repo`)

### Token Not Working
- Make sure you copied the entire token (starts with `ghp_`)
- Check if your organization requires SSO authorization for tokens
- Verify the token hasn't been revoked

### Clear Stored Credentials
If you need to update stored credentials:

**Windows:**
- Open "Credential Manager" → "Windows Credentials"
- Find and delete GitHub entries

**macOS:**
- Open "Keychain Access"
- Search for "github" and delete entries

**Linux - WSL:**
- Delete `~/.git-credentials` file

## When to Use SSH Instead

Consider switching to SSH keys if you:
- Use Git frequently (multiple times per day)
- Work on multiple machines
- Want more security
- Are in a professional development environment
- Find token management annoying

SSH is more complex to set up but more convenient long-term.

---

**Quick Reference:**
- Token URL: https://github.com/settings/personal-access-tokens/new
- Scope needed: `repo`
- Use token as password when prompted
- Tokens start with `ghp_`