# Deployment Guide - Vercel

This guide will help you deploy your Tijaniyah Muslim Pro landing page to Vercel.

## Prerequisites

- GitHub account (✅ Already set up)
- Vercel account (Sign up at https://vercel.com if you don't have one)

## Deployment Steps

### Option 1: Deploy via Vercel Dashboard (Recommended)

1. **Go to Vercel**
   - Visit https://vercel.com
   - Sign in with your GitHub account

2. **Import Your Repository**
   - Click "Add New..." → "Project"
   - Select your repository: `bvggies/tijaniyahmuslimproweb`
   - Click "Import"

3. **Configure Project**
   - **Framework Preset**: Other (or leave as default)
   - **Root Directory**: `./` (default)
   - **Build Command**: Leave empty (static site)
   - **Output Directory**: Leave empty (serves from root)
   - **Install Command**: Leave empty (no dependencies)

4. **Deploy**
   - Click "Deploy"
   - Wait for deployment to complete (usually 1-2 minutes)

5. **Access Your Site**
   - Vercel will provide you with a URL like: `https://tijaniyahmuslimproweb.vercel.app`
   - Your site is now live! 🎉

### Option 2: Deploy via Vercel CLI

1. **Install Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy**
   ```bash
   vercel
   ```
   - Follow the prompts
   - Choose your project settings
   - Deploy!

4. **Production Deploy**
   ```bash
   vercel --prod
   ```

## Custom Domain (Optional)

1. Go to your project dashboard on Vercel
2. Click "Settings" → "Domains"
3. Add your custom domain
4. Follow the DNS configuration instructions

## Automatic Deployments

Vercel automatically deploys:
- **Production**: Every push to `main` branch
- **Preview**: Every push to other branches or pull requests

## Environment Variables

If you need to add environment variables later:
1. Go to Project Settings → Environment Variables
2. Add your variables
3. Redeploy

## Troubleshooting

### Build Fails
- Check that `vercel.json` is in the root directory
- Ensure all files are committed and pushed to GitHub

### 404 Errors
- Verify `index.html` is in the root directory
- Check `vercel.json` configuration

### Images Not Loading
- Ensure images are in the `assets/` folder
- Check image paths in `index.html` (should be `assets/filename.jpg`)

## Need Help?

- Vercel Documentation: https://vercel.com/docs
- Vercel Support: https://vercel.com/support

