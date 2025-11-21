/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  images: {
    unoptimized: true,
  },
  // Use basePath for GitHub Pages deployment
  // The trailing slash in assetPrefix is important for proper asset loading
  basePath: process.env.NODE_ENV === 'production' ? '/Assistent-Agent-' : '',
  assetPrefix: process.env.NODE_ENV === 'production' ? '/Assistent-Agent-' : '',
  trailingSlash: true,
}

module.exports = nextConfig
