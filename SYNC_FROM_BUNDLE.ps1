# SYNC_FROM_BUNDLE.ps1
# Applies the sandbox repo state (full git history) into the local Windows
# repo, then optionally pushes to GitHub.
#
# SETUP (once):
#   1. Download LINKEDIN_EMPIRE_BACKUP_2026-10-09.zip and extract it to
#      C:\Users\USER\Downloads\emphire_sync
#   2. Copy this script into the SAME folder as linkedin_emphire_full.bundle
#
# RUN (from that folder):
#   powershell -NoProfile -ExecutionPolicy Bypass -File .\SYNC_FROM_BUNDLE.ps1
#
# Push auth: git will prompt. Username = your GitHub handle, password =
# Personal Access Token (repo scope). The PAT is never stored by this script.

$ErrorActionPreference = 'Continue'
$Repo   = 'C:\Users\USER\Desktop\PROJECTS\LINKEDINEMPHIRE'
$Bundle = Join-Path $PSScriptRoot 'linkedin_emphire_full.bundle'
$Remote = 'https://github.com/Teamthy/linkedin_emphire.git'

Write-Host '==> LinkedIn Empire sync from bundle'

if (-not (Get-Command git -ErrorAction SilentlyContinue)) { throw 'git not found in PATH' }
if (-not (Test-Path $Bundle)) { throw "bundle not found next to script: $Bundle" }

if (-not (Test-Path (Join-Path $Repo '.git'))) {
    # No repo yet -> clone from bundle and wire origin to GitHub
    Write-Host "==> No repo at $Repo - cloning fresh from bundle"
    if (Test-Path $Repo) { throw "$Repo exists but is not a git repo - rename/move it first, then re-run" }
    git clone -b main $Bundle $Repo
    if ($LASTEXITCODE -ne 0) { throw 'clone failed' }
    Set-Location $Repo
    git remote remove origin 2>$null | Out-Null
    git remote add origin $Remote
} else {
    Set-Location $Repo
    Write-Host "==> Repo root: $Repo"

    $hasOrigin = (git remote) -match '^origin$'
    if (-not $hasOrigin) { git remote add origin $Remote }

    $dirty = git status --porcelain
    if ($dirty) {
        Write-Host '!! Uncommitted changes exist in the local repo:'
        $dirty | ForEach-Object { Write-Host "    $_" }
        Write-Host '   Commit or stash them first, e.g.:'
        Write-Host '     git add -A ; git commit -m "local: notes from windows"'
        Write-Host '   (or) git stash  - then re-run this script.'
        throw 'dirty working tree'
    }

    $branch = (git rev-parse --abbrev-ref HEAD).Trim()
    if ($branch -ne 'main') { git checkout main }

    Write-Host '==> Fetching bundle history'
    git branch -D emphire_sync 2>$null | Out-Null
    git fetch $Bundle 'refs/heads/main:emphire_sync'
    if ($LASTEXITCODE -ne 0) { throw 'bundle fetch failed' }

    Write-Host '==> Applying'
    git merge --ff-only emphire_sync
    if ($LASTEXITCODE -ne 0) {
        Write-Host '    (no fast-forward: local history diverged - doing a real merge)'
        git merge --no-edit emphire_sync
        if ($LASTEXITCODE -ne 0) {
            git merge --abort
            Write-Host '!! MERGE CONFLICT. Stop. Show me: git status'
            throw 'conflict - needs manual resolution'
        }
    }
    git branch -D emphire_sync | Out-Null
}

Write-Host ''
Write-Host '==> Synced. Latest 3 commits now in the local repo:'
git log --oneline -3
Write-Host ''
$push = Read-Host 'Push to GitHub now? (y/N)'
if ($push -match '^\s*[yY]') {
    Write-Host '==> Pushing to origin/main (git will prompt for GitHub username + PAT as password)'
    git push origin main
    if ($LASTEXITCODE -eq 0) { Write-Host '==> PUSHED. GitHub now matches the sandbox. Done.' }
    else { Write-Host '!! Push failed. Try your push_to_github.ps1, or re-check the PAT (needs repo scope).' }
} else {
    Write-Host '==> Not pushed. Whenever ready, from the repo folder:'
    Write-Host '     git push origin main   (or)  .\push_to_github.ps1'
}
Write-Host ''
Write-Host 'NEXT (standing habit, after every Friday review):'
Write-Host '  cd /home-side repo is auto-committed here; on Windows re-run this whole flow'
Write-Host '  or simply: git pull origin main  ->  work  ->  commit  ->  push.'
