const express = require("express");
const cors = require("cors");

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

let appointments = [
  { id: 1, name: "Ivan Horvat", service: "Muško šišanje", time: "Pon 10:00" },
];
let nextId = 2;

app.get("/api/health", (req, res) => {
  res.json({ status: "ok", timestamp: new Date().toISOString() });
});

app.get("/api/termini", (req, res) => {
  res.json(appointments);
});

app.post("/api/termini", (req, res) => {
  const { name, service, time } = req.body;
  if (!name || !service || !time) {
    return res.status(400).json({ error: "name, service i time su obavezni" });
  }
  const appointment = { id: nextId++, name, service, time };
  appointments.push(appointment);
  res.status(201).json(appointment);
});

app.delete("/api/termini/:id", (req, res) => {
  const id = Number(req.params.id);
  const before = appointments.length;
  appointments = appointments.filter((a) => a.id !== id);
  if (appointments.length === before) {
    return res.status(404).json({ error: "termin nije pronadjen" });
  }
  res.status(204).send();
});

app.listen(PORT, () => {
  console.log(`Backend server sluša na portu ${PORT}`);
});
