import "./globals.css";

export const metadata = {
  title: "OmniLearn AI",
  description: "OmniLearn AI: adaptive AI courses with lessons, resources, and mastery tracking.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
