// =============================================================
//  300 Deutsche Verben - module app logic
//  Expects VERBS (array) and CATID (int) defined before this file.
// =============================================================
const N = VERBS.length;
const KEY = 'gv-progress-' + CATID;

const TTS = (() => {
  const u = ('speechSynthesis' in window) ? window.speechSynthesis : null;
  let voice = null;
  if (u) {
    const pick = () => {
      const vs = u.getVoices();
      voice = vs.find(v => v.lang === 'de-DE') || vs.find(v => v.lang && v.lang.slice(0, 2) === 'de') || null;
    };
    pick();
    u.onvoiceschanged = pick;
  }
  return {
    ok: !!u,
    speak(t) {
      if (!u) return;
      u.cancel();
      const x = new SpeechSynthesisUtterance(t);
      x.lang = 'de-DE';
      x.rate = 0.92;
      if (voice) x.voice = voice;
      u.speak(x);
    }
  };
})();

window.speak = function (t) { TTS.speak(t); };

function escHtml(s) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function q(tag, attrs, html) {
  const el = document.createElement(tag);
  for (const k in attrs) el.setAttribute(k, attrs[k]);
  if (html != null) el.innerHTML = html;
  return el;
}

// ---------- progress ----------
function setProg(p) {
  p = Math.max(0, Math.min(100, Math.round(p)));
  localStorage.setItem(KEY, p);
  const f = document.getElementById('progFill');
  const t = document.getElementById('progPct');
  if (f) f.style.width = p + '%';
  if (t) t.textContent = p + '%';
}
function getProg() { return parseInt(localStorage.getItem(KEY) || '0', 10); }
function resetProg() {
  if (confirm('Fortschritt zurücksetzen?')) {
    localStorage.removeItem(KEY);
    setProg(0);
  }
}
setProg(getProg());

// ---------- tabs ----------
document.querySelectorAll('.tabbtn').forEach(b => b.addEventListener('click', () => {
  document.querySelectorAll('.tabbtn').forEach(x => x.classList.remove('active'));
  document.querySelectorAll('.panel').forEach(x => x.classList.remove('active'));
  b.classList.add('active');
  document.getElementById('panel-' + b.dataset.tab).classList.add('active');
}));

// ---------- helpers ----------
function shuffle(a) {
  const arr = a.slice();
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

// Full infinitive without the reflexive "sich/mich/dich" part
function infinitiveOf(v) {
  return String(v).replace(/^(sich|mich|dich)\s+/i, '');
}

// Main verb stem: infinitive minus separable prefix + reflexive + (e)n ending
function verbRoot(vv) {
  let s = infinitiveOf(vv);
  const prefixes = ['zurück', 'zusammen', 'entgegen', 'vorbei', 'weiter', 'mit', 'nach', 'vor', 'aus', 'auf', 'an',
    'ab', 'bei', 'ein', 'los', 'zu', 'teil', 'fern', 'fest'];
  for (const p of prefixes) {
    if (s.startsWith(p) && s.length > p.length + 3) { s = s.slice(p.length); break; }
  }
  let root = s.replace(/(en|ern|eln)$/, '');
  if (root.length < 3) root = s.replace(/en$/, '');
  if (root.length < 3) root = s;
  return root;
}

// ---------- cloze builder (shared by Lücken & Quiz) ----------
function clozeFor(v) {
  const root = verbRoot(v.v);
  if (root.length < 3) return null;
  const re = new RegExp('\\b(' + root.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')[a-zäöüß]*\\b', 'i');
  for (const c of [{ s: v.example, label: 'Beispiel' }, { s: v.natural, label: 'Natürlicher' }]) {
    const m = c.s.match(re);
    if (m) {
      return {
        blanked: c.s.slice(0, m.index) + '______' + c.s.slice(m.index + m[0].length),
        original: c.s,
        label: c.label,
        hit: m[0]
      };
    }
  }
  return null;
}

// 4 full-infinitive options (1 correct + 3 distractors)
function verbOptions(correctVerb) {
  const seen = new Set([infinitiveOf(correctVerb).toLowerCase()]);
  const opts = [correctVerb];
  const pool = shuffle(VERBS.map(v => v.v));
  for (const w of pool) {
    const key = infinitiveOf(w).toLowerCase();
    if (!seen.has(key)) { seen.add(key); opts.push(w); }
    if (opts.length === 4) break;
  }
  while (opts.length < 4) opts.push(correctVerb);
  return shuffle(opts);
}

// simple grammar category for the Grammatik question type
function gramTag(v) {
  const g = (v.grammar || '').toLowerCase();
  if (g.indexOf('trennbar') > -1) return 'trennbar';
  if (g.indexOf('reflexiv') > -1) return 'reflexiv';
  if (g.indexOf('modalverb') > -1) return 'Modalverb';
  if (g.indexOf('hilfsverb') > -1) return 'Hilfsverb';
  if (g.indexOf('starkes verb') > -1) return 'starkes Verb';
  return 'regelmäßig';
}

// ---------- study ----------
(function () {
  const list = document.getElementById('studyList');
  VERBS.forEach((v, i) => {
    const tags = escHtml(v.grammar).split('·').map(g => `<span class="gramtag">${g.trim()}</span>`).join('');
    const card = q('div', { className: 'qcard' }, `
      <div class="reveal" style="margin:0">
        <div class="g"><span class="speak" data-speak="verb">${escHtml(v.v)}</span>
          <span class="en">– ${escHtml(v.en)}</span> ${tags}
          <span style="float:right;color:var(--grey);font-size:.8rem">${i + 1} / ${N}</span>
        </div>
        <div style="margin-top:.6rem"><em>${escHtml(v.meaning)}</em></div>
        <div style="margin-top:.5rem"><b>Beispiel:</b> <span class="speak" data-speak="example">${escHtml(v.example)}</span></div>
        <div style="margin-top:.35rem;color:var(--grey)"><b>Natürlicher:</b> <span class="speak" data-speak="natural">${escHtml(v.natural)}</span></div>
      </div>`);
    card.querySelectorAll('.speak[data-speak]').forEach(sp => {
      sp.addEventListener('click', e => {
        e.stopPropagation();
        const kind = sp.dataset.speak;
        TTS.speak(kind === 'verb' ? v.v : kind === 'example' ? v.example : v.natural);
      });
    });
    list.appendChild(card);
  });
})();

// ---------- drill (flashcards) ----------
let drillOrder = shuffle([...Array(N).keys()]);
let drillIdx = 0;

function setDrill() {
  const v = VERBS[drillOrder[drillIdx]];
  const card = document.getElementById('flipcard');
  card.classList.remove('flipped');
  const verbEl = document.getElementById('drillVerb');
  verbEl.className = 'verb speak';
  verbEl.textContent = v.v;
  verbEl.onclick = (e) => { e.stopPropagation(); TTS.speak(v.v); };
  document.getElementById('drillEn').textContent = v.en + ' · ' + v.meaning;
  document.getElementById('drillSent').innerHTML =
    '<b>Beispiel:</b> ' + escHtml(v.example) + '<br><b>Natürlicher:</b> ' + escHtml(v.natural);
  document.getElementById('drillPos').textContent = (drillIdx + 1) + ' / ' + N;
  document.getElementById('drillFill').style.width = ((drillIdx + 1) / N * 100) + '%';
}
function flip() { document.getElementById('flipcard').classList.toggle('flipped'); }
function drillNext() {
  if (drillIdx === N - 1) {
    drillOrder = shuffle([...Array(N).keys()]);
    drillIdx = 0;
  } else {
    drillIdx++;
  }
  setDrill();
  setProg(getProg() + Math.max(1, Math.round(100 / N)));
}
function drillPrev() {
  if (drillIdx === 0) { setDrill(); return; }
  drillIdx--;
  setDrill();
}
setDrill();

// =============================================================
//  LÜCKEN (Welches Verb passt?)
// =============================================================
const ROUND_LEN = 10;
let fillItems = [], fillIdx = 0, fillScore = 0, fillAnswered = 0;

function fillScoreElt() { return document.getElementById('fillScore'); }

function genFill() {
  fillItems = shuffle(VERBS.map((v, i) => ({ v, i }))).slice(0, ROUND_LEN);
  fillIdx = 0; fillScore = 0; fillAnswered = 0;
  fillShow();
}

function fillProgress() {
  document.getElementById('fillPos').textContent = (fillIdx + 1) + ' / ' + ROUND_LEN;
  document.getElementById('fillFill').style.width = ((fillIdx + 1) / ROUND_LEN * 100) + '%';
  if (fillScoreElt()) fillScoreElt().textContent = fillScore + ' / ' + fillAnswered + ' richtig';
}

function fillShow() {
  fillProgress();
  const it = fillItems[fillIdx];
  const v = VERBS[it.i];
  const cloze = clozeFor(v);
  const opts = verbOptions(v.v);

  let inner;
  if (cloze) {
    inner = `
      <p class="qtype">Welches Verb passt in den Satz? <span class="qtype-tag">${cloze.label}</span></p>
      <div class="q"><em>„${escHtml(cloze.blanked)}“</em>
        <span class="speak inline" data-say="${escHtml(cloze.original)}">🔊 anhören</span></div>
      <div class="opts">${opts.map(o => `<button class="opt" data-ok="${o === v.v ? '1' : '0'}">${escHtml(o)}</button>`).join('')}</div>`;
  } else {
    // fallback: meaning-based (if no sentence could be blanked)
    inner = `
      <p class="qtype">Welches Verb passt zur Bedeutung?</p>
      <div class="q"><em>„${escHtml(v.meaning)}“</em></div>
      <div class="opts">${opts.map(o => `<button class="opt" data-ok="${o === v.v ? '1' : '0'}">${escHtml(o)}</button>`).join('')}</div>`;
  }
  const box = q('div', { className: 'qcard' }, inner + `<div id="fillFb"></div>`);
  box.querySelectorAll('.opt').forEach(b => b.addEventListener('click', () => fillPick(b, v)));
  box.querySelectorAll('.speak[data-say]').forEach(sp => sp.addEventListener('click', e => { e.stopPropagation(); TTS.speak(sp.dataset.say); }));
  const host = document.getElementById('fillQ');
  host.innerHTML = '';
  host.appendChild(box);
}

function fillPick(btn, v) {
  if (btn.disabled) return;
  boxdisabled('#fillQ .opt');
  const ok = btn.dataset.ok === '1';
  btn.classList.add(ok ? 'correct' : 'wrong');
  fillAnswered++;
  if (ok) fillScore++;

  const cloze = clozeFor(v);
  const fb = document.getElementById('fillFb');
  const sol = cloze
    ? `Die Lösung: <span class="speak" data-sol="${escHtml(cloze.original)}">„${escHtml(cloze.original)}“</span>`
    : `Die Lösung: <b>${escHtml(v.v)}</b>`;

  fb.innerHTML = (ok
    ? `<div class="feedback ok">Richtig! 🎉</div>`
    : `<div class="feedback no">Nicht ganz – <b>${escHtml(v.v)}</b> (${escHtml(v.en)})</div>`)
    + `<div class="feedback sol">${sol}</div>`;

  fb.querySelectorAll('.speak').forEach(sp => sp.addEventListener('click', e => { e.stopPropagation(); TTS.speak(sp.dataset.sol); }));

  fillProgress();
  setProg(getProg() + 1);

  const btnWrap = q('div', { className: 'navbtns' },
    fillIdx < ROUND_LEN - 1
      ? `<button class="btn">Weiter →</button>`
      : `<button class="btn">Ergebnis anzeigen 🏁</button>`);
  btnWrap.querySelector('button').addEventListener('click', () => {
    if (fillIdx < ROUND_LEN - 1) { fillIdx++; fillShow(); }
    else fillResult();
  });
  fb.appendChild(btnWrap);
}

function fillResult() {
  const host = document.getElementById('fillQ');
  host.innerHTML = '';
  const card = q('div', { className: 'qcard results' }, `
    <h3>🏁 Runde geschafft</h3>
    <p class="bigscore">Du hast <b>${fillScore}</b> von <b>${ROUND_LEN}</b> Sätzen richtig ergänzt.</p>
    <div class="navbtns">
      <button class="btn" id="fillAgain">Nochmal spielen</button>
      <button class="btn ghost" onclick="document.querySelector('[data-tab=drill]').click()">Zu den Karten</button>
    </div>`);
  card.querySelector('#fillAgain').addEventListener('click', genFill);
  host.appendChild(card);
  fillProgress();
}
function boxdisabled(sel) { [...document.querySelectorAll(sel)].forEach(o => o.disabled = true); }
function fillReset() { genFill(); }
genFill();

// =============================================================
//  QUIZ
// =============================================================
let quizItems = [], quizIdx = 0, quizScore = 0, quizAnswered = 0;

function quizScoreElt() { return document.getElementById('quizScore'); }

function genQuiz() {
  quizItems = shuffle(VERBS.map((v, i) => ({ v, i }))).slice(0, ROUND_LEN);
  quizIdx = 0; quizScore = 0; quizAnswered = 0;
  quizShow();
}

function quizProgress() {
  document.getElementById('quizPos').textContent = (quizIdx + 1) + ' / ' + ROUND_LEN;
  document.getElementById('quizFill').style.width = ((quizIdx + 1) / ROUND_LEN * 100) + '%';
  if (quizScoreElt()) quizScoreElt().textContent = quizScore + ' / ' + quizAnswered + ' richtig';
}

function quizShow() {
  quizProgress();
  const it = quizItems[quizIdx];
  const v = VERBS[it.i];

  // pick the question type for this item (fixed per item -> predictable)
  const tpl = (it.i * 7 + quizIdx) % 4;
  const pool = shuffle(VERBS.filter(x => x.i !== it.i));

  let badge, qhtml, opts, correct = v.v;

  if (tpl === 0) {            // Englisch -> Deutsch
    badge = 'Englisch → Deutsch';
    qhtml = `Wie heißt dieses Verb auf Deutsch? <span class="speak inline" data-say="${escHtml(v.v)}">🔊 anhören</span>`;
    opts = verbOptions(v.v);
  } else if (tpl === 1) {     // Deutsch -> Englisch
    badge = 'Deutsch → Englisch';
    correct = v.en;
    qhtml = `Was bedeutet „<b>${escHtml(v.v)}</b>“?`;
    const seen = new Set([v.en]); const o = [v.en];
    for (const d of pool) { if (!seen.has(d.en.toLowerCase())) { seen.add(d.en.toLowerCase()); o.push(d.en); } if (o.length === 4) break; }
    opts = shuffle(o);
  } else if (tpl === 2) {     // Satz -> Welches Verb?
    badge = 'Im Satz';
    const cloze = clozeFor(v);
    correct = v.v;
    if (cloze) {
      qhtml = `Welches Verb passt in den Satz? <span class="speak inline" data-say="${escHtml(cloze.original)}">🔊 anhören</span>
        <div class="q" style="margin-top:.6rem"><em>„${escHtml(cloze.blanked)}“</em></div>`;
    } else {
      qhtml = `Welches Verb hat diese Bedeutung? „<em>${escHtml(v.meaning)}</em>“`;
    }
    opts = verbOptions(v.v);
  } else {                    // Grammatik
    badge = 'Grammatik';
    correct = gramTag(v);
    const tags = ['trennbar', 'reflexiv', 'Modalverb', 'Hilfsverb', 'starkes Verb', 'regelmäßig'];
    opts = shuffle([correct].concat(tags.filter(t => t !== correct)).slice(0, 3));
    qhtml = `Zu welchem Typ gehört „<b>${escHtml(v.v)}</b>“?`;
  }

  const box = q('div', { className: 'qcard' }, `
    <p class="qtype"><span class="qtype-tag">${badge}</span></p>
    <div class="q">${qhtml}</div>
    <div class="opts">${opts.map(o => `<button class="opt" data-v="${escHtml(String(o)).replace(/"/g, '&quot;')}" data-ok="${String(o) === String(correct) ? '1' : '0'}">${escHtml(o)}</button>`).join('')}</div>
    <div id="quizFb"></div>`);
  box.querySelectorAll('.opt').forEach(b => b.addEventListener('click', () => quizPick(b, String(correct), v)));
  box.querySelectorAll('.speak[data-say]').forEach(sp => sp.addEventListener('click', e => { e.stopPropagation(); TTS.speak(sp.dataset.say); }));
  const host = document.getElementById('quizQ');
  host.innerHTML = '';
  host.appendChild(box);
}

function quizPick(btn, correct, v) {
  if (btn.disabled) return;
  boxdisabled('#quizQ .opt');
  const ok = btn.dataset.ok === '1';
  btn.classList.add(ok ? 'correct' : 'wrong');
  quizAnswered++;
  if (ok) quizScore++;

  const fb = document.getElementById('quizFb');
  let extra = '';
  if (btn.dataset.ok !== '1') extra = `<div class="feedback sol">Antwort: <b>${escHtml(correct)}</b></div>`;
  fb.innerHTML = (ok
    ? `<div class="feedback ok">Richtig! 🎉</div>`
    : `<div class="feedback no">Leider falsch.</div>`)
    + extra;

  quizProgress();
  setProg(getProg() + 1);

  const btnWrap = q('div', { className: 'navbtns' },
    quizIdx < ROUND_LEN - 1
      ? `<button class="btn">Weiter →</button>`
      : `<button class="btn">Ergebnis anzeigen 🏁</button>`);
  btnWrap.querySelector('button').addEventListener('click', () => {
    if (quizIdx < ROUND_LEN - 1) { quizIdx++; quizShow(); }
    else quizResult();
  });
  fb.appendChild(btnWrap);
}

function quizResult() {
  const host = document.getElementById('quizQ');
  host.innerHTML = '';
  const card = q('div', { className: 'qcard results' }, `
    <h3>🏁 Quiz geschafft</h3>
    <p class="bigscore">Du hast <b>${quizScore}</b> von <b>${ROUND_LEN}</b> Fragen richtig beantwortet.</p>
    <div class="navbtns">
      <button class="btn" id="quizAgain">Nochmal spielen</button>
      <button class="btn ghost" onclick="document.querySelector('[data-tab=drill]').click()">Zu den Karten</button>
    </div>`);
  card.querySelector('#quizAgain').addEventListener('click', genQuiz);
  host.appendChild(card);
  quizProgress();
}
function quizReset() { genQuiz(); }
genQuiz();