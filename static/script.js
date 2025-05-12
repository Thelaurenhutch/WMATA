function loadTrains() {
  const code = document.getElementById("station").value;
  fetch(`/api/arrivals/${code}`)
    .then(res => res.json())
    .then(data => {
      const list = document.getElementById("results");
      list.innerHTML = '';
      data.Trains.forEach(train => {
        const li = document.createElement("li");
        li.textContent = `${train.Line} train to ${train.Destination} in ${train.Min} min`;
        list.appendChild(li);
      });
    });
}
