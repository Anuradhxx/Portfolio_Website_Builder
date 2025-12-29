let skillsContainer;
let skillCount = 0;

document.addEventListener("DOMContentLoaded", () => {
    skillsContainer = document.getElementById("skillsContainer");

    if (!skillsContainer) {
        console.error("skillsContainer not found in DOM");
        return;
    }

    loadSkills();
});

// Add a new skill input
function addSkillField(name = "", level = 0) {
    skillCount++;

    const skillDiv = document.createElement("div");
    skillDiv.classList.add("skills-form");

    skillDiv.innerHTML = `
        <div class="form-group">
            <label>Skill ${skillCount}</label>
            <input type="text" placeholder="e.g. Python" value="${name}" required>
        </div>

        <div class="form-group">
            <label>Proficiency level (0–5)</label>
            <input type="number" min="0" max="5" value="${level}" required>
        </div>

        <div class="skill-progress">
            <div class="skill-progress-bar">
                <div class="progress-fill" style="width:${level * 20}%"></div>
            </div>
            <div class="progress-text">${level * 20}%</div>
        </div>
    `;

    skillsContainer.appendChild(skillDiv);

    const levelInput = skillDiv.querySelector("input[type=number]");
    const fill = skillDiv.querySelector(".progress-fill");
    const text = skillDiv.querySelector(".progress-text");

    levelInput.addEventListener("input", () => {
        const val = Math.min(Math.max(Number(levelInput.value), 0), 5);
        fill.style.width = `${val * 20}%`;
        text.textContent = `${val * 20}%`;
    });
}

// Load existing skills
async function loadSkills() {
    try {
        const res = await fetch("/api/skills");
        const skills = await res.json();

        skillsContainer.innerHTML = "";
        skillCount = 0;

        if (skills.length === 0) {
            addSkillField();
        } else {
            skills.forEach(skill =>
                addSkillField(skill.name, skill.proficiency_level)
            );
        }
    } catch (err) {
        console.error("Load failed:", err);
        addSkillField();
    }
}

// Save skills
async function saveSkills() {
    const forms = skillsContainer.querySelectorAll(".skills-form");

    if (forms.length === 0) {
        alert("No skills to save");
        return;
    }

    for (const form of forms) {
        const name = form.querySelector("input[type=text]").value.trim();
        const level = Number(form.querySelector("input[type=number]").value);

        if (!name) continue;

        await fetch("/api/skills/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                name,
                proficiency_level: level
            })
        });
    }

    alert("Skills saved successfully");
    loadSkills();
}
