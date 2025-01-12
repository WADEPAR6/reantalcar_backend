/** @type {import('next').NextConfig} */
const nextConfig = {
  eslint: {
    ignoreDuringBuilds: true,
  },
  reactStrictMode: true,
  typescript: {
    ignoreBuildErrors: true,
  },
  images: {
    remotePatterns: [
      {
        protocol: "https",
        hostname: "**", // Coincide con cualquier dominio
        port: "", // Sin restricciones de puerto
        pathname: "**", // Coincide con cualquier ruta
      },
    ],
  },
};
export default nextConfig;
