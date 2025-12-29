// app/static/js/auth.js

document.addEventListener("DOMContentLoaded", () => {

    // LOGIN
    const loginForm = document.getElementById("loginForm");
    if (loginForm) {
        loginForm.addEventListener("submit", async (e) => {
            e.preventDefault();

            const email = loginForm.email.value;
            const password = loginForm.password.value;

            const res = await fetch("/auth/login", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                credentials: "include",
                body: JSON.stringify({ email, password })
            });

            const data = await res.json();

            if (!res.ok) {
                alert(data.detail || "Login failed");
                return;
            }

            // store token
            // localStorage.setItem("access_token", data.access_token);


            // redirect
            window.location.href = "/dashboard/";
        });
    }

    // REGISTER
    
    const registerForm = document.getElementById("registerForm");
    if (registerForm) {
        registerForm.addEventListener("submit", async (e) => {
            e.preventDefault();

            const payload = {
                username: registerForm.username.value,
                email: registerForm.email.value,
                password: registerForm.password.value
            };

            // 1️⃣ Register user
            const registerRes = await fetch("/auth/register", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify(payload)
            });

            if (!registerRes.ok) {
                const err = await registerRes.json();
                alert(err.detail || "Registration failed");
                return;
            }

            // 2️⃣ Auto-login user
            const loginRes = await fetch("/auth/login", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                credentials: "include",
                body: JSON.stringify({
                    email: payload.email,
                    password: payload.password
                })
            });

            if (!loginRes.ok) {
                alert("Login failed after registration");
                return;
            }

            // 3️⃣ Redirect to dashboard
            window.location.href = "/dashboard/";
        });
    }

    //logout

      const logoutBtn = document.getElementById("logoutBtn");
      if (logoutBtn) {
          logoutBtn.addEventListener("click", async () => {
            await fetch("/auth/logout", {
              method: "POST",
              credentials: "include"
            });

          window.location.href = "/login";
        });
      }

});

