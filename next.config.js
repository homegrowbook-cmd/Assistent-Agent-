/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  images: {
    unoptimized: true,
  },
  basePath: process.env.NODE_ENV === 'production' ? '/Assistent-Agent-' : '',
  assetPrefix: process.env.NODE_ENV === 'production' ? '/Assistent-Agent-/' : '',
}

module.exports = nextConfig
