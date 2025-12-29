document.addEventListener("DOMContentLoaded", fetchProfile);

async function fetchProfile() {
  try {
    const res = await fetch("/api/profile", {
      headers: { "Authorization": "Bearer " + localStorage.getItem("token") }
    });
    if (!res.ok) throw new Error("Cannot fetch profile");
    const data = await res.json();
    document.getElementById("name").value = data.name;
    document.getElementById("bio").value = data.bio;
  } catch (err) {
    alert(err.message);
  }
}

async function saveProfile() {
  try {
    const res = await fetch("/api/profile", {
      method: "PUT",
      headers: {
        "Authorization": "Bearer " + localStorage.getItem("token"),
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        name: document.getElementById("name").value,
        bio: document.getElementById("bio").value
      })
    });
    if (!res.ok) throw new Error("Failed to update profile");
    alert("Profile updated successfully");
  } catch (err) {
    alert(err.message);
  }
}
