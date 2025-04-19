# Guide to Upload Your Repository to GitHub

This guide will walk you through the process of uploading your local Git repository to GitHub.

## Step 1: Create a GitHub Account

If you don't already have a GitHub account:
1. Go to [GitHub](https://github.com/)
2. Click "Sign up" and follow the instructions to create your account

## Step 2: Create a New Repository on GitHub

1. Log in to your GitHub account
2. Click the "+" icon in the top-right corner and select "New repository"
3. Enter a name for your repository (e.g., "python-training")
4. (Optional) Add a description
5. Keep the repository as "Public" if you want anyone to see it, or select "Private" if you want to restrict access
6. Do NOT initialize the repository with a README, .gitignore, or license as you already have these files locally
7. Click "Create repository"

## Step 3: Connect Your Local Repository to GitHub

After creating the repository, GitHub will show you instructions. Follow the "push an existing repository from the command line" section.

Run these commands in your terminal (replace `YOUR-USERNAME` with your actual GitHub username and `REPO-NAME` with your repository name):

```bash
git remote add origin https://github.com/YOUR-USERNAME/REPO-NAME.git
git branch -M main
git push -u origin main
```

### What these commands do:
- `git remote add origin`: Links your local repository to your GitHub repository
- `git branch -M main`: Renames your default branch to "main" (GitHub's standard)
- `git push -u origin main`: Uploads your code to GitHub and sets up tracking

## Step 4: Verify Your Upload

1. Go to your GitHub repository page (https://github.com/YOUR-USERNAME/REPO-NAME)
2. You should see all your files, including the README which will be displayed on the main page

## Making Future Changes

After making changes to your local files:

```bash
git add .                                   # Stage all changes
git commit -m "Description of your changes" # Commit changes
git push                                    # Push to GitHub
```

## Using GitHub Authentication

When pushing to GitHub for the first time, you'll need to authenticate. GitHub no longer supports simple password authentication for Git operations. Instead:

### Option 1: Use HTTPS with a Personal Access Token (Recommended)
1. Go to GitHub → Settings → Developer settings → Personal access tokens → Generate new token
2. Give it a name, set an expiration, and select the "repo" scope
3. Generate the token and copy it
4. When Git asks for your password, use this token instead

### Option 2: Use SSH Authentication
1. Generate an SSH key pair if you don't have one: `ssh-keygen -t ed25519 -C "your.email@example.com"`
2. Add the public key to your GitHub account (Settings → SSH and GPG keys)
3. Use the SSH URL when adding the remote: `git remote add origin git@github.com:YOUR-USERNAME/REPO-NAME.git`

## Getting Help

If you encounter any issues, refer to [GitHub's documentation](https://docs.github.com/en) or use the GitHub Community forums.