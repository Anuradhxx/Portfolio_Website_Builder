document.addEventListener("DOMContentLoaded", fetchProjects);

async function fetchProjects() {
  try {
    const res = await fetch("/api/projects", {
      headers: { "Authorization": "Bearer " + localStorage.getItem("token") }
    });
    if (!res.ok) throw new Error("Cannot fetch projects");
    const data = await res.json();
    const container = document.getElementById("projects");
    container.innerHTML = "";
    data.forEach(project => {
      const div = document.createElement("div");
      div.classList.add("project-card");
      div.innerHTML = `<h3>${project.title}</h3><p>${project.description}</p>`;
      container.appendChild(div);
    });
  } catch (err) {
    alert(err.message);
  }
}

async function addProject() {
  const title = document.getElementById("title").value;
  const desc = document.getElementById("desc").value;
  if (!title || !desc) return alert("Fill all fields");

  try {
    const res = await fetch("/api/projects", {
      method: "POST",
      headers: {
        "Authorization": "Bearer " + localStorage.getItem("token"),
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ title, description: desc })
    });
    if (!res.ok) throw new Error("Failed to add project");
    document.getElementById("title").value = "";
    document.getElementById("desc").value = "";
    fetchProjects();
  } catch (err) {
    alert(err.message);
  }
}
