(function () {
  const box = document.getElementById("gl-lookup");
  const input = document.getElementById("gl-query");
  const out = document.getElementById("gl-results");
  if (!box || !input || !out) return;
  const esc = (s) => String(s || "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const rank = { must: "must", should: "should", mention: "mention", none: "none", not_assessed: "none", source_unavailable: "none" };
  let index = null;

  function findColumns(query) {
    const q = query.toLowerCase().trim();
    const terms = q.split(/\s+/).filter(Boolean);
    const matches = new Set();
    if (!q || !index) return [];
    Object.entries(index.keywords).forEach(([keyword, columns]) => {
      const k = keyword.toLowerCase();
      if (q.includes(k) || terms.some((term) => k.includes(term) || term.includes(k))) columns.forEach((column) => matches.add(column));
    });
    return Array.from(matches).sort();
  }

  function emptyState() {
    const list = Object.entries(index.columns).map(([id, col]) => `<li><button type="button" data-col="${id}">${id} ${esc(col.name)}</button></li>`).join("");
    out.innerHTML = `<p class="gl-empty">該当コラムなし。キーワードを変えてください。</p><ul class="gl-columns">${list}</ul>`;
  }

  function renderColumn(id) {
    const col = index.columns[id];
    const cells = col.cells.map((cell) => `<li class="gl-cell"><div><span class="gl-guide">${esc(cell.guideline)}</span><span class="gl-strength ${rank[cell.strength] || "none"}">${esc(cell.strength)}</span></div><p>${esc(cell.summary)}</p><a href="${esc(cell.citation_url)}" target="_blank" rel="noopener">原文リンク</a><span class="gl-confidence">${esc(cell.confidence)}</span></li>`).join("");
    return `<section class="gl-column"><h2>${id} ${esc(col.name)}</h2><ol>${cells}</ol></section>`;
  }

  function search(query) {
    const columns = findColumns(query);
    if (!columns.length) return emptyState();
    out.innerHTML = columns.map(renderColumn).join("");
  }

  function wireSuggestButtons() {
    const input = document.getElementById('gl-query');
    document.querySelectorAll('.gl-suggest-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        input.value = btn.dataset.query;
        input.dispatchEvent(new Event('input'));
        input.focus();
      });
    });
  }

  fetch("assets/lookup-index.json").then((r) => r.json()).then((data) => {
    index = data;
    emptyState();
    input.addEventListener("input", () => search(input.value));
    wireSuggestButtons();
    out.addEventListener("click", (e) => {
      if (e.target.dataset && e.target.dataset.col) {
        input.value = e.target.textContent;
        out.innerHTML = renderColumn(e.target.dataset.col);
      }
    });
  }).catch(() => { out.innerHTML = '<p class="gl-empty">検索インデックスを読み込めませんでした。</p>'; });
})();
