const form = document.getElementById("booking-form");
const nameInput = document.getElementById("name");
const serviceInput = document.getElementById("service");
const timeInput = document.getElementById("time");
const list = document.getElementById("appointments");

async function loadAppointments() {
  try {
    const res = await fetch(`${API_BASE_URL}/api/termini`);
    const data = await res.json();
    renderAppointments(data);
  } catch (err) {
    list.innerHTML = `<li>Greška pri dohvaćanju termina.</li>`;
  }
}

function renderAppointments(appointments) {
  list.innerHTML = "";
  if (appointments.length === 0) {
    list.innerHTML = `<li>Trenutno nema zakazanih termina.</li>`;
    return;
  }
  for (const a of appointments) {
    const li = document.createElement("li");
    li.innerHTML = `
      <span><strong>${a.name}</strong> - ${a.service}
        <span class="meta">${a.time}</span>
      </span>
      <button class="delete-btn" data-id="${a.id}">Otkaži</button>
    `;
    list.appendChild(li);
  }
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const name = nameInput.value.trim();
  const service = serviceInput.value;
  const time = timeInput.value.trim();
  if (!name || !service || !time) return;

  try {
    await fetch(`${API_BASE_URL}/api/termini`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, service, time }),
    });
    form.reset();
    await loadAppointments();
  } catch (err) {
    alert("Rezervacija nije uspjela. Provjeri je li backend pokrenut.");
  }
});

list.addEventListener("click", async (e) => {
  if (!e.target.matches(".delete-btn")) return;
  const id = e.target.dataset.id;
  try {
    await fetch(`${API_BASE_URL}/api/termini/${id}`, { method: "DELETE" });
    await loadAppointments();
  } catch (err) {
    alert("Otkazivanje nije uspjelo.");
  }
});

loadAppointments();
