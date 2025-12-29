async function publish() {
  try {
    const res = await fetch("/api/portfolio/publish", {
      method: "POST",
      headers: {
        "Authorization": "Bearer " + localStorage.getItem("token")
      }
    });
    if (!res.ok) throw new Error("Failed to publish portfolio");
    alert("Portfolio published successfully!");
  } catch (err) {
    alert(err.message);
  }
}
