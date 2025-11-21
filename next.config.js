/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  images: {
    unoptimized: true,
  },
  // Use basePath for GitHub Pages deployment
  // basePath and assetPrefix must match exactly (no trailing slash) for proper asset loading
  basePath: process.env.NODE_ENV === 'production' ? '/Assistent-Agent-' : '',
  assetPrefix: process.env.NODE_ENV === 'production' ? '/Assistent-Agent-' : '',
  trailingSlash: true,
}

module.exports = nextConfig
