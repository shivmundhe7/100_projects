# Rebuilding the UI with basic CSS for the AuthPage form
# Adding styles and updating App.jsx for consistent UI

# Update files with styled UI
styled_files = {
    f"{base_dir}/src/pages/AuthPage.jsx": """
import { useState } from "react";
import { supabase } from "../supabaseClient";
import "./AuthPage.css";

export default function AuthPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    const { error } = await supabase.auth.signInWithPassword({
      email,
      password,
    });
    if (error) alert("Login Error: " + error.message);
  };

  return (
    <div className="auth-container">
      <div className="auth-card">
        <div className="logo">🎤</div>
        <h2>AI Assistant</h2>
        <p>Sign in to your account</p>
        <form onSubmit={handleLogin}>
          <input
            type="email"
            placeholder="Enter your email"
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <input
            type="password"
            placeholder="Enter your password"
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <button type="submit">Sign In</button>
        </form>
        <p className="signup-text">
          Don’t have an account? <a href="#">Sign up</a>
        </p>
      </div>
    </div>
  );
}
""",

    f"{base_dir}/src/pages/AuthPage.css": """
.auth-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: #f9fafb;
}

.auth-card {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  text-align: center;
  width: 100%;
  max-width: 400px;
}

.auth-card h2 {
  margin: 0.5rem 0;
}

.auth-card .logo {
  font-size: 2rem;
  color: #6c5ce7;
}

.auth-card form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-top: 1rem;
}

.auth-card input {
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 1rem;
}

.auth-card button {
  padding: 0.75rem;
  background: #6c5ce7;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: bold;
}

.signup-text {
  margin-top: 1rem;
  font-size: 0.9rem;
}
"""
}

# Write styled files
for filepath, content in styled_files.items():
    with open(filepath, "w") as f:
        f.write(content.strip())

# Update the zip with the new styles
with ZipFile(zip_path, "w") as zipf:
    for foldername, _, filenames in os.walk(base_dir):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            zipf.write(file_path, os.path.relpath(file_path, base_dir))

zip_path
